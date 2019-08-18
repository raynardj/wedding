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
    print("READING FROM DB")
    from .. import db
    return list(q.line_html for q in db.session.query(quoteModel).all())

class photoView(ModelView):
    datamodel = SQLAInterface(quoteModel)
    route_base = "/quotes"

    add_columns = ["line"]
    edit_columns = ["line"]
    list_columns = ["line_html", "created_by"]

    @expose()
    def showquote(self):
        if "qimg" not in session :
            session["qimg"] = imglist
        if "qlines" not in session:
            session["qlines"] = get_all_quotes()
        if len(session["qimg"]) ==0:
            session["qimg"] = imglist
        if len(session["qlines"]) == 0:
            session["qlines"] = get_all_quotes()

        waiting = session["qimg"]
        img_url = random.choice(waiting)
        waiting.remove(img_url)
        session["qimg"] = waiting
        session["lastimg"] = img_url

        unspoken = session["qlines"]
        qline = random.choice(unspoken)
        unspoken.remove(qline)
        session["qlines"] = unspoken
        session["lastline"] = qline

        return self.render_template("quotes.html",
                                    img_url = img_url,
                                    quote = qline)