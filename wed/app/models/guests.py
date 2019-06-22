from . import db
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin

class guestTypeModel(Model,AuditMixin):
    __tablename__ = "guest_type"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    remark = db.Column(db.Text())

    def __repr__(self):
        return self.name

    @property
    def gcount(self):
        return sum(list(g.gcount for g in self.guests))

class guestModel(Model,AuditMixin):
    __tablename__ = "guest"
    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer(),db.ForeignKey(guestTypeModel.id))
    type = db.relationship(guestTypeModel)
    fullname = db.Column(db.Text())
    plus = db.Column(db.Integer(), default = 0)
    babies = db.Column(db.Integer(), default = 0)
    phone = db.Column(db.Text(),nullable = True)
    ishotel = db.Column(db.Boolean(), default = False)
    hotel = db.Column(db.Text(), nullable=True)
    ispickup = db.Column(db.Boolean(), default=False)
    pickup = db.Column(db.Text(), nullable=True)
    invitation = db.Column(db.Boolean(), default = False)
    remark = db.Column(db.Text(), nullable = True)

    def __repr__(self):
        plus = " +%s位"%(self.plus) if self.plus >0 else ""
        babies = " +%s位小孩"%(self.babies) if self.babies >0 else ""
        return "%s%s%s"%(self.fullname,plus,babies)

    @property
    def gcount(self):
        """guest number count for this guest"""
        return 1+self.plus

guestTypeModel.guests = db.relationship(guestModel)