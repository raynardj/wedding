from flask_appbuilder import ModelView, expose
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface

from wed.app.models.guests import guestTypeModel, guestModel
from flask import request
from flask_login import current_user

class guestTypeView(ModelView):
    route_base = "/gtype"
    datamodel = SQLAInterface(guestTypeModel)
    show_title = "宾客类型"
    add_title = "添加宾客类型"
    edit_title = "编辑宾客类型"
    list_title = "宾客大类"
    label_columns = {"name":"类型名称","remark":"备注","guests":"包含宾客"}

    add_columns = ["name","remark"]
    edit_columns = ["name", "remark"]
    list_columns = ["name","remark","guests"]

    @expose("/detail/<gtype_id>/")
    def detail(self,gtype_id):
        gtype = self.datamodel.get(int(gtype_id))
        return self.render_template("gtype_detail.html", gtype = gtype)


class guestView(ModelView):
    route_base = "/guest"
    datamodel = SQLAInterface(guestModel)
    show_title = "宾客"
    add_title = "添加宾客"
    edit_title = "修改宾客信息"
    list_title = "宾客编辑列表"
    label_columns = {"fullname":"宾客全名","type":"宾客种类","babies":"携带宝宝数","phone":"手机",
                     "ishotel":"需安排住宿","ispickup":"需车辆接送","hotel":"酒店详情","pickup":"接送详情",
                     "invitation":"已发请柬","remark":"备注"
                     }
    add_columns = ["fullname", "type","plus","babies","phone","invitation",
                   "remark","ishotel","hotel","ispickup","pickup"]
    edit_columns = ["fullname", "type","plus", "babies", "phone", "invitation",
                   "remark", "ishotel", "hotel", "ispickup", "pickup"]
    list_columns = ["fullname", "type","remark",  "phone", "invitation",
                     "ishotel",  "ispickup","babies",]

    @expose("/all/")
    def all(self):
        guests = self.datamodel.session.query(guestModel).all()
        guest_total = self.datamodel.session.query(guestModel).count()+sum(list(g.plus for g in guests))
        return self.render_template("all.html",guests = guests, guest_total = guest_total)

    @expose("/babies/")
    def babies(self):
        babyguest = self.datamodel.session.query(guestModel).filter(guestModel.babies>0).all()
        babycount = sum(list(bg.babies for bg in babyguest))
        print(babyguest)
        return self.render_template("babies.html", babyguest = babyguest, babycount = babycount)