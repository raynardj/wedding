from flask_appbuilder import ModelView, expose, BaseView
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface

from wed.app.models.photo import photoModel
from flask import request
from flask_login import current_user
from .. import app
from wed.app.models.photo import quoteModel
import os

imglist = os.listdir(app.root_path+"/static/images/rj/")
import random

def get_all_quotes():
    from .. import db
    return list(q.line_html for q in db.session.query(quoteModel).all())

quotes_list = get_all_quotes()

class photoView(ModelView):
    datamodel = SQLAInterface(quoteModel)
    route_base = "/quotes"

    add_columns = ["line"]
    edit_columns = ["line"]
    list_columns = ["line_html", "created_by"]

    @expose()
    def showquote(self):
        return self.render_template("quotes.html",
                                    img_url = random.choice(imglist),
                                    quote = random.choice(quotes_list))