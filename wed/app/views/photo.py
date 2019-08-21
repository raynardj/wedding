from flask_appbuilder import ModelView, expose, BaseView
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface

from wed.app.models.photo import photoModel
from flask import request, session
from flask_login import current_user
from .. import app
from wed.app.models.photo import quoteModel
import os

imglist = os.listdir(app.root_path+"/static/images/rj/")
import random
import logging

# def get_all_quotes():
#     from .. import db
#     return list(q.line_html for q in db.session.query(quoteModel).all())
#
# quotes_list = get_all_quotes()
from datetime import datetime
def dcache(span=10):
    """
    A python dictionary cache decorator
    span : length of cache, in seconds , default 10
    """
    c = dict({})
    def inner(f):
        def func():
            now = int(datetime.now().timestamp())//span
            if "now" in c:
                if c["now"] == now:
                    return c["store"]
            c["now"] = now
            store = f()
            c["store"]=store
            return store
        return func
    return inner

@dcache(span=60)
def get_all_quotes():
    from .. import db
    return list(q.line_html for q in db.session.query(quoteModel).all())

class photoView(ModelView):
    datamodel = SQLAInterface(quoteModel)
    route_base = "/quotes"

    add_columns = ["line"]
    edit_columns = ["line"]
    list_columns = ["line_html", "created_by"]

    @expose()
    @expose("/<strs>/")
    def showquote(self,strs = ""):
        if "qimg" not in session :
            session["qimg"] = imglist
        if "qlines" not in session:
            session["qlines"] = get_all_quotes()

        waiting = session["qimg"]
        if len(waiting) ==0: # replenish img list
            print("replenishing image list")
            waiting = imglist

        unspoken = session["qlines"]
        if len(unspoken) == 0: # replenish quotes list
            print("replenishing quote list")
            unspoken = get_all_quotes()

        try:
            img_url = random.choice(waiting)
            waiting.remove(img_url)
        except Exception as e:
            img_url = random.choice(imglist)
            logging.error(str(e))
        session["qimg"] = waiting
        try:
            qline = random.choice(unspoken)
            unspoken.remove(qline)
        except Exception as e:
            qline = random.choices(get_all_quotes())
            logging.error(str(e))
        session["qlines"] = unspoken

        lastbtn = {"line":session["lastline"],
                   "img":session["lastimg"]} if ("lastline" in session) and ("lastimg" in session) else False

        session["lastimg"] = img_url
        session["lastline"] = qline
        return self.render_template("quotes.html",
                                    nexturl = hex(random.randint(10000, 20000)),
                                    lastbtn = lastbtn,
                                    img_url = img_url,
                                    quote = qline)

    @expose("/last/")
    def lastquote(self):
        img_url = request.args.get("img")
        qline = request.args.get("line")
        return self.render_template("quotes.html",
                                    nexturl=hex(random.randint(10000, 20000)),
                                    img_url=img_url,
                                    quote=qline)