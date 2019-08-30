from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView

from .. import appbuilder, db
from .guests import guestTypeView,guestView,dinnerView
from .photo import photoView

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )

appbuilder.add_view_no_menu(guestTypeView)
appbuilder.add_view_no_menu(guestView)
appbuilder.add_view_no_menu(photoView)



appbuilder.add_link("宾客名单","/guest/all/", icon="fa-address-book",category_label="宾客",
                    category="guests",category_icon="fa-address-card")
appbuilder.add_link("编辑宾客列表","/guest/list/", icon="fa-address-book",category_label="宾客",
                    category="guests",category_icon="fa-address-card")

appbuilder.add_link("添加宾客","/guest/add", icon="fa-user-plus",category_label="宾客",
                    category="guests",category_icon="fa-address-card")

appbuilder.add_view(dinnerView,"分桌列表", icon="fa-hand-peace-o",
                    category_label="宾客",category="guests", category_icon="fa-address-card")

appbuilder.add_link("分组列表","/gtype/all/", icon="fa-group",category_label="宾客",
                    category="guests",category_icon="fa-address-card")

appbuilder.add_link("添加分组","/gtype/add", icon="fa-beer",category_label="宾客",
                    category="guests",category_icon="fa-address-card")

appbuilder.add_link("宝宝清单","/guest/babies/", icon="fa-child",category_label="特别关注",
                    category="attention",category_icon="fa-heart")

appbuilder.add_link("住宿清单","/guest/hotel/", icon="fa-bed",category_label="特别关注",
                    category="attention",category_icon="fa-heart")

appbuilder.add_link("接送清单","/guest/pickup/", icon="fa-taxi",category_label="特别关注",
                    category="attention",category_icon="fa-heart")

appbuilder.add_link("爱情骗人的话", "/quotes/list/", icon="fa-language",category_label="甜蜜",
                    category="love",category_icon="fa-heart")

db.create_all()
