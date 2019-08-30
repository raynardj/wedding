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

    @property
    def moneyshow(self):
        return sum(list(g.redpack if g.redpack else 0 for g in self.guests))

class dinnerModel(Model,AuditMixin):
    __tablename__ = "dinner"
    id = db.Column(db.Integer, primary_key=True)
    sn = db.Column(db.Text,default="<Table>")
    remark = db.Column(db.Text)

    @property
    def guest_number(self):
        return sum(list(g.gcount for g in self.guests))

class guestModel(Model,AuditMixin):
    __tablename__ = "guest"
    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer(),db.ForeignKey(guestTypeModel.id))
    type = db.relationship(guestTypeModel)
    fullname = db.Column(db.Text())
    # describe = db.Column(db.Text(),nullable=True)
    plus = db.Column(db.Integer(), default = 0)
    babies = db.Column(db.Integer(), default = 0)
    phone = db.Column(db.Text(),nullable = True)
    ishotel = db.Column(db.Boolean(), default = False)
    hotel = db.Column(db.Text(), nullable=True)
    ispickup = db.Column(db.Boolean(), default=False)
    pickup = db.Column(db.Text(), nullable=True)
    invitation = db.Column(db.Boolean(), default = False)
    redpack = db.Column(db.Integer(), default=0)
    remark = db.Column(db.Text(), nullable = True)
    dinner_id = db.Column(db.Integer,db.ForeignKey(dinnerModel.id))
    dinner = db.relationship(dinnerModel, backref = "guests")

    def __repr__(self):
        plus = " +%s位"%(self.plus) if self.plus >0 else ""
        babies = " +%s位小孩"%(self.babies) if self.babies else ""
        return "%s%s%s"%(self.fullname,plus,babies)

    @property
    def gcount(self):
        """guest number count for this guest"""
        return 1+(self.plus if self.plus else 0)

guestTypeModel.guests = db.relationship(guestModel)

