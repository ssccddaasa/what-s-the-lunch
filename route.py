from main import *
from formss import *
import secrets
import os
from random import sample



def saveImg0(imgname):
    ranHex = secrets.token_hex(8)
    _, ext = os.path.splitext(imgname.filename)
    picname = ranHex + ext
    picpath = os.path.join(a.root_path, "static/user_pics", picname)
    imgname.save(picpath)
    return picname

def saveImg(imgname):
    ranHex = secrets.token_hex(8)
    _, ext = os.path.splitext(imgname.filename)
    picname = ranHex + ext
    picpath = os.path.join(a.root_path, "static/res_pics", picname)
    imgname.save(picpath)
    return picname

def saveImg2(imgname):
    ranHex = secrets.token_hex(8)
    _, ext = os.path.splitext(imgname.filename)
    picname = ranHex + ext
    picpath = os.path.join(a.root_path, "static", picname)
    imgname.save(picpath)
    return picname

def deleteImg(imgname):
    PicPath = os.path.join(a.root_path, "static",imgname)
    try:
        os.remove(PicPath)
    except:
        pass



@a.route("/", methods=["GET","POST"])
def START():
    if(current_user.is_authenticated):
        if (session.get("user")):
            return redirect(url_for("hi2"))
        else:
            return redirect(url_for("hi"))

    return render_template("chose.html", title="Start")

@a.route("/hi")
def hi():
    with a.app_context():
        with db.engine.connect() as con:
            sc = text("select * from meal;")
            x = con.execute(sc)
    meals = x
    m1 = []
    for y in meals:
        m1.append(y)

    if(len(m1)>5):
        mm1 = sample(m1,5)
    else:
        mm1 = m1

    with a.app_context():
        with db.engine.connect() as con:
            sc2 = text("select * from meal order by price;")
            x2 = con.execute(sc2)
    meals2 = x2

    m2 = []
    for y in meals2:
        m2.append(y)

    if (len(m2) > 5):
        mm2 = m2[:5]
    else:
        mm2 = m2
    return render_template("index.html", meals=mm1,meals2=mm2)





@a.route("/hi2")
def hi2():
    with a.app_context():
        with db.engine.connect() as con:
            sc = text("select * from meal;")
            x = con.execute(sc)
    meals = x
    m1 = []
    for y in meals:
        m1.append(y)

    if(len(m1)>5):
        mm1 = sample(m1,5)
    else:
        mm1 = m1

    with a.app_context():
        with db.engine.connect() as con:
            sc2 = text("select * from meal order by price;")
            x2 = con.execute(sc2)
    meals2 = x2

    m2 = []
    for y in meals2:
        m2.append(y)

    if (len(m2) > 5):
        mm2 = m2[:5]
    else:
        mm2 = m2
    return render_template("index2.html", meals=mm1,meals2=mm2)





@a.route("/reg", methods=["GET","POST"])
def REG():
  formi = UserReg()
  if (formi.validate_on_submit()):
      hash_pass = bcr.generate_password_hash(formi.password.data).decode("utf-8")
      UserSiUp = user(formi.name.data,formi.maile.data,hash_pass,formi.phone.data,formi.location.data)
      with a.app_context():
          db.session.add(UserSiUp)
          db.session.commit()
      flash(f"okey okey", category="success")
      return redirect(url_for("logg"))
  return render_template("reg.html", title="reg", form= formi)









@a.route("/reg2", methods=["GET","POST"])
def REG2():
  formi = ResReg()
  if (formi.validate_on_submit()):
      hash_pass = bcr.generate_password_hash(formi.password.data).decode("utf-8")
      ResSiUp = restaurant(formi.resname.data,formi.maile.data,hash_pass,formi.phone.data,formi.location.data,formi.type.data)
      with a.app_context():
          db.session.add(ResSiUp)
          db.session.commit()
      flash(f"okey okey res res res res", category="success")
      return redirect(url_for("logg2"))
  return render_template("regres.html", title="regres", form= formi)







@a.route("/add", methods=["GET","POST"])
@login_required
def ADDM():
  formi = MealAdd()
  img = url_for('static', filename=f'res_pics/meeaal.png')
  if (formi.validate_on_submit()):
      picfile = saveImg2(formi.image.data)
      imname = picfile
      mealaddd = meal(formi.name.data,formi.type.data,formi.des.data,formi.price.data,current_user.get_id(),imname)
      with a.app_context():
          db.session.add(mealaddd)
          db.session.commit()
      flash(f"okey okey addddddddddddddddddddd", category="success")
      return redirect(url_for("hi"))
  return render_template("addmeal.html", title="addmeal", form= formi, img=img)





@a.route("/log", methods=["GET","POST"])
def logg():
  formi = log()
  if (formi.validate_on_submit()):
      UserSin = user.query.filter_by(name=formi.name.data).first()
      if(UserSin and bcr.check_password_hash(UserSin.password, formi.password.data)):
          login_user(UserSin, remember=formi.remb.data)
          session["user"] = "user"
          flash(f"okey ya ya ya okey", category="success")
          return redirect(url_for("hi2"))
      else:
          flash(f"no no no no !!!", category="danger")
  return render_template("log.html", title="reg", form= formi)





@a.route("/log2", methods=["GET","POST"])
def logg2():
  formi = log2()
  if (formi.validate_on_submit()):
      ResSin = restaurant.query.filter_by(resName=formi.resname.data).first()
      if(ResSin and bcr.check_password_hash(ResSin.password, formi.password.data)):
          login_user(ResSin, remember=formi.remb.data)
          flash(f"okey ya ya ya okey res res res", category="success")
          return redirect(url_for("hi"))
      else:
          flash(f"no no no no !!!", category="danger")
  return render_template("logres.html", title="logres", form= formi)


@a.route("/logout")
def logout():
    logout_user()
    session["user"] = None
    flash(f"we log out yeaaaaaah", category="success")
    return redirect(url_for("START"))



@a.route("/pro/<int:resID>", methods=["GET","POST"])
def PRO(resID):
    if(current_user.id != resID):
        res = restaurant.query.filter_by(id=resID).first()
        img = url_for('static', filename=f'res_pics/{current_user.image}')
        return render_template("prostat.html", res=res,img=img)
    elif(current_user.id == resID):
        return redirect(url_for("PROV"))



@a.route("/pro2/<int:resID>", methods=["GET","POST"])
def PRO2(resID):
    res = restaurant.query.filter_by(id=resID).first()
    img = url_for('static', filename=f'res_pics/{current_user.image}')
    tru = res_user.query.filter_by(resId=resID, id=int(current_user.id)).first()
    return render_template("prostat2.html", res=res, img=img, tru=tru)


@a.route("/pro/v", methods=["GET", "POST"])
@login_required
def PROV():
    idd = current_user.id
    meals = meal.query.filter_by(resId= current_user.id).all()
    with a.app_context():
        with db.engine.connect() as con:
            sc = text('''select m.title, u.name
                         from meal m inner join orderr o
                         on m.meal_number = o.meal_number
                         inner join user u
                         on o.id = u.id
                         where o.resId = ''' + str(idd) + ";")
            x = con.execute(sc)
    orddd = x
    formi = ProResReg()
    if (formi.validate_on_submit()):
        if formi.image.data:
            picfile = saveImg(formi.image.data)
            current_user.image = picfile
        current_user.resName = formi.resname.data
        current_user.email = formi.maile.data
        current_user.type = formi.type.data
        current_user.Description = formi.des.data
        current_user.location = formi.location.data
        current_user.phone = formi.phone.data
        db.session.commit()
        flash(f"your profile is updated", category="success")
        return redirect(url_for("PROV"))
    elif (request.method == "GET"):
        formi.resname.data = current_user.resName
        formi.maile.data = current_user.email
        formi.type.data = current_user.type
        formi.des.data = current_user.Description
        formi.location.data = current_user.location
        formi.phone.data = current_user.phone
        img = url_for('static', filename=f'res_pics/{current_user.image}')
    return render_template("proval.html", title="profile", form=formi, img=img,meals=meals, orddd=orddd)




@a.route("/pro2/v2", methods=["GET", "POST"])
@login_required
def PROV2():
    idd = current_user.id
    with a.app_context():
        with db.engine.connect() as con:
            sc = text('''select r.resName, r.id 
            from res_user rs inner join restaurant r 
            on rs.resId = r.id 
            where rs.id = '''+str(idd)+ ";")
            x = con.execute(sc)
    cart = x
    us = user.query.filter_by(id=int(current_user.id)).first()
    img = url_for('static', filename=f'user_pics/{us.image}')
    formi = UserPro()
    if (formi.validate_on_submit()):
        if formi.image.data:
            picfile = saveImg0(formi.image.data)
            us.image = picfile
        us.name = formi.name.data
        us.email = formi.maile.data
        us.location = formi.location.data
        us.phone = formi.phone.data
        db.session.commit()
        flash(f"your profile is updated", category="success")
        return redirect(url_for("PROV2"))
    elif (request.method == "GET"):
        formi.name.data = us.name
        formi.maile.data = us.email
        formi.location.data = us.location
        formi.phone.data = us.phone
    return render_template("proval2.html", title="profile", form=formi, img=img, us=us, cart=cart)



@a.route("/ord/<mnum>", methods=["GET", "POST"])
def MEALORD(mnum):
    formi = ord()
    meall = meal.query.filter_by(meal_number=mnum).first()
    idd = int(meall.resId)
    res = restaurant.query.filter_by(id=idd).first()
    if(formi.validate_on_submit()):
        order = orderr(int(meall.resId),int(current_user.id),int(meall.meal_number))
        with a.app_context():
            db.session.add(order)
            db.session.commit()
        flash(f"order has been sent", category="success")
    return render_template("mealord.html", meall=meall,form=formi,res=res)


@a.route("/cart/<rnum>", methods=["GET", "POST"])
def CART(rnum):
    cart = res_user(int(rnum),int(current_user.id))
    with a.app_context():
        db.session.add(cart)
        db.session.commit()
    return redirect(url_for("hi2"))











@a.route("/mel/up/<mealnum>", methods=["GET", "POST"])
@login_required
def MEALUP(mealnum):
    meals = meal.query.filter_by(meal_number=mealnum).first()
    formi = MealAdd()
    if (formi.validate_on_submit()):
        if formi.image.data:
            deleteImg(meals.image)
            picfile = saveImg2(formi.image.data)
            meals.image = picfile


        meals.title = formi.name.data
        meals.price = formi.price.data
        meals.type = formi.type.data
        meals.Description = formi.des.data
        db.session.commit()
        flash(f"your meal is updated", category="success")
        return redirect(url_for("MEALUP", mealnum=mealnum))
    elif (request.method == "GET"):

        formi.name.data = meals.title
        formi.price.data = meals.price
        formi.type.data = meals.type
        formi.des.data = meals.Description

        img = url_for('static', filename=meals.image)
    return render_template("updmeal.html", title="UP meal", form=formi, img=img)


@a.route("/mel/del/<mealnum>", methods=["GET","POST"])
def MEALDEL(mealnum):
    meals = meal.query.filter_by(meal_number=mealnum).first()
    deleteImg(meals.image)
    db.session.delete(meals)
    db.session.commit()
    flash(f"your meal is deleted", category="success")
    return redirect(url_for("PROV"))


@a.route("/mel/show/<cat>", methods=["GET","POST"])
def MEALSHOW(cat):
    st = ""
    if(cat == "rand"):
        with a.app_context():
            with db.engine.connect() as con:
                sc = text("select * from meal;")
                x = con.execute(sc)
        meals = x
        st = "كل الوجبات"

    elif(cat == "cheap"):
        with a.app_context():
            with db.engine.connect() as con:
                sc = text("select * from meal order by price;")
                x = con.execute(sc)
        meals = x
        st = "الأرخص"
    else:
        meals = meal.query.filter_by(type=cat).all()
        st = cat

    return render_template("mealshow.html", meals=meals, st=st)


@a.route("/mel2/show/<cat>", methods=["GET","POST"])
def MEALSHOW2(cat):
    st = ""
    if(cat == "rand"):
        with a.app_context():
            with db.engine.connect() as con:
                sc = text("select * from meal;")
                x = con.execute(sc)
        meals = x
        st = "كل الوجبات"

    elif(cat == "cheap"):
        with a.app_context():
            with db.engine.connect() as con:
                sc = text("select * from meal order by price;")
                x = con.execute(sc)
        meals = x
        st = "الأرخص"
    else:
        meals = meal.query.filter_by(type=cat).all()
        st = cat

    return render_template("mealshow2.html", meals=meals, st=st)


if __name__ == "__main__":
    a.run(debug=True)