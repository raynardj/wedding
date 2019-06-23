from flask_appbuilder import ModelView, expose
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface

from wed.app.models.photo import photoModel
from flask import request
from flask_login import current_user

class photoView(ModelView):
    datamodel = SQLAInterface(photoModel)
    route_base = "/album"

    show_title = "查看相片"
    add_title = "上传相片"

    label_columns = {"photo":"照片","name":"名称", "remark":"备注"}

    add_columns = ["photo","name","remark"]
    list_columns = ["photo_img"]