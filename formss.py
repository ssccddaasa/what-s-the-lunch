from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField, TextAreaField, FileField, SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError
from main import user, restaurant, current_user


class UserReg(FlaskForm):
    name = StringField("الاسم", validators=[DataRequired(), Length(2, 30)])
    maile = StringField("الايميل", validators=[DataRequired(), Email()])
    phone = StringField("رقم الهاتف", validators=[DataRequired(), Length(8, 30)])
    location = StringField("الموقع", validators=[DataRequired(), Length(2, 250)])
    password = PasswordField("كلمة السر", validators=[DataRequired(), Regexp("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")])
    cpassword = PasswordField("تأكيد كلمة السر", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("إنشاء حساب")

    def validate_name(self, name):
        temp = user.query.filter_by(name=name.data).first()
        if temp:
            raise ValidationError("name already exists!")

    def validate_maile(self, maile):
        temp = user.query.filter_by(email= maile.data).first()
        if temp:
            raise ValidationError("email already exists!")


class UserPro(FlaskForm):
    name = StringField("الاسم", validators=[DataRequired(), Length(2, 30)])
    maile = StringField("الايميل", validators=[DataRequired(), Email()])
    phone = StringField("رقم الهاتف", validators=[DataRequired(), Length(8, 30)])
    location = StringField("الموقع", validators=[DataRequired(), Length(2, 250)])
    image = FileField("تحديث الصورة", validators=[FileAllowed(["jpg", 'png'])])
    submit = SubmitField("تحديث")

    def validate_name(self, name):
        us = user.query.filter_by(id=int(current_user.id)).first()
        if (name.data != us.name):
            temp = user.query.filter_by(name=name.data).first()
            if temp:
                raise ValidationError("name already exists!")

    def validate_maile(self, maile):
        us = user.query.filter_by(id=int(current_user.id)).first()
        if (maile.data != us.email):
            temp = user.query.filter_by(email=maile.data).first()
            if temp:
                raise ValidationError("email already exists!")






class ResReg(FlaskForm):
    resname = StringField("اسم المطعم", validators=[DataRequired(), Length(2, 30)])
    maile = StringField("الايميل", validators=[DataRequired(), Email()])
    phone = StringField("رقم الهاتف", validators=[DataRequired(), Length(8, 30)])
    type = SelectField("اختصاص المطعم", validators=[DataRequired()],choices=[("تقليدي","تقليدي"),("وجبات سريعة","وجبات سريعة"),("حلويات","حلويات"),("قهوة","قهوة"),("أخرى","أخرى")])
    location = StringField("الموقع", validators=[DataRequired(), Length(2, 250)])
    password = PasswordField("كلمة السر", validators=[DataRequired(), Regexp("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")])
    cpassword = PasswordField("تأكيد كلمة السر", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("إنشاء")

    def validate_resname(self, resname):
        temp = restaurant.query.filter_by(resName=resname.data).first()
        if temp:
            raise ValidationError("name already exists!")

    def validate_maile(self, maile):
        temp = restaurant.query.filter_by(email= maile.data).first()
        if temp:
            raise ValidationError("email already exists!")






class log(FlaskForm):
    name = StringField("الاسم", validators=[DataRequired(), Length(2,30)])
    password = PasswordField("كلمة السر", validators=[DataRequired()])
    remb = BooleanField("تذكرني")
    submit = SubmitField("تسجيل الدخول")


class log2(FlaskForm):
    resname = StringField("اسم المطعم", validators=[DataRequired(), Length(2,30)])
    password = PasswordField("كلمة السر", validators=[DataRequired()])
    remb = BooleanField("تذكرني")
    submit = SubmitField("تسجيل الدخول")




class MealAdd(FlaskForm):
    name = StringField("اسم الوجبة", validators=[DataRequired(), Length(2, 30)])
    type = SelectField("النوع", validators=[DataRequired()],choices=[("طبيخ","طبيخ"),("بيتزا","بيتزا"),("شاورما","شاورما"),("برغر","برغر"),("مقبلات","مقبلات"),("مقالي","مقالي"),("حلويات","حلويات"),("عصائر","عصائر"),("أخرى","أخرى")])
    price = FloatField("السعر",validators=[DataRequired()])
    des = TextAreaField("الوصف",validators=[DataRequired()])
    image = FileField("صورة الوجبة", validators=[FileAllowed(["jpg", 'png'])])
    submit = SubmitField("تم")




class ProResReg(FlaskForm):
    resname = StringField("اسم المطعم",validators=[DataRequired(), Length(2, 30)])
    maile = StringField("الايميل",validators=[DataRequired(), Email()])
    phone = StringField("رقم الهاتف", validators=[DataRequired(), Length(8, 30)])
    type = SelectField("اختصاص المطعم", validators=[DataRequired()],choices=[("تقليدي","تقليدي"),("وجبات سريعة","وجبات سريعة"),("حلويات","حلويات"),("قهوة","قهوة"),("أخرى","أخرى")])
    location = StringField("الموقع",validators=[DataRequired(), Length(2, 250)])
    des = TextAreaField("الوصف العام",validators=[DataRequired()])
    image = FileField("تحديث الصورة",validators=[FileAllowed(["jpg", 'png'])])
    submit = SubmitField("تحديث")

    def validate_resname(self, resname):
        if (resname.data != current_user.resName):
            temp = restaurant.query.filter_by(resName=resname.data).first()
            if temp:
                raise ValidationError("name already exists!")

    def validate_maile(self, maile):
        if (maile.data != current_user.email):
            temp = restaurant.query.filter_by(email= maile.data).first()
            if temp:
                raise ValidationError("email already exists!")



class ord(FlaskForm):
    submit = SubmitField("Order")