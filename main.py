from flask import Flask, render_template, flash, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user,login_manager, current_user, login_required, logout_user
#from flask_uploads import UploadSet, IMAGES, configure_uploads






a = Flask(__name__)
a.config["SECRET_KEY"] = 'e9a918c7419bc27ee98a4f04f4b8a32daa6a26a3dd4fb707d1514808861a10df'
a.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:13542687Qwe@localhost/lunch"
a.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(a)
bcr = Bcrypt(a)
login = LoginManager(a)



@login.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))

@login.user_loader
def load_user(user_id):
    return restaurant.query.get(int(user_id))

#meal = db.relationship("meal", backref="owner", lazy=True)
class user(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False,unique=True)
    email = db.Column(db.String(100), nullable=False,unique=True)
    password = db.Column(db.String(150), nullable=False,unique=True)
    location = db.Column(db.String(250), nullable=False)
    image = db.Column(db.String(50), nullable=False,default="default2.png")
    phone = db.Column(db.String(25), nullable=False)
    cart = db.relationship("res_user", backref="user", lazy=True)
    revs = db.relationship("orderr", backref="user", lazy=True)

    def __init__(self,name,email,password,phone,location):
        self.name = name
        self.email = email
        self.password = password
        self.location = location
        self.phone = phone

    def __repr__(self):
        return f"User: ({self.name}/ {self.email})"





class restaurant(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    resName = db.Column(db.String(25), nullable=False,unique=True)
    email = db.Column(db.String(100), nullable=False,unique=True)
    password = db.Column(db.String(150), nullable=False,unique=True)
    location = db.Column(db.String(250), nullable=False)
    type = db.Column(db.String(25), nullable=False,default='مطعم')
    Description = db.Column(db.String(1000), nullable=False)
    image = db.Column(db.String(50), nullable=False, default="default.png")
    phone = db.Column(db.String(25), nullable=False)
    meal = db.relationship("meal", backref="restaurant", lazy=True)
    cart = db.relationship("res_user", backref="restaurant", lazy=True)
    sender = db.relationship("orderr", backref="restaurant", lazy=True)

    def __init__(self,resName,email,password,phone,location,type):
        self.resName = resName
        self.email = email
        self.password = password
        self.location = location
        self.phone = phone
        self.Description = "res"
        self.type = type

    def __repr__(self):
        return f"User: ({self.resName}/ {self.email})"






class meal(db.Model):
    meal_number = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25), nullable=False)
    type = db.Column(db.String(25), nullable=False, default='طبيخ')
    Description = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(50), nullable=False, default="default3.png")
    resId = db.Column(db.Integer, db.ForeignKey("restaurant.id"),  nullable=False)
    objj = db.relationship("orderr", backref="meal", lazy=True)

    def __init__(self, title,type,Description,price,resid,image):
        self.title = title
        self.type = type
        self.Description = Description
        self.price = price
        self.resId = resid
        self.image = image

    def __repr__(self):
        return f"Meal: ({self.title}/ {self.price})"





class res_user(db.Model):
    resId = db.Column(db.Integer,db.ForeignKey("restaurant.id"), primary_key=True)
    id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)

    def __init__(self, resId, id):
        self.resId = resId
        self.id = id


class orderr(db.Model):
    ordnum = db.Column(db.Integer, primary_key=True)
    resId = db.Column(db.Integer,db.ForeignKey("restaurant.id"))
    id = db.Column(db.Integer, db.ForeignKey("user.id"))
    meal_number = db.Column(db.Integer, db.ForeignKey("meal.meal_number"))

    def __init__(self, resId,id,meal_number):
        self.resId = resId
        self.id = id
        self.meal_number = meal_number






