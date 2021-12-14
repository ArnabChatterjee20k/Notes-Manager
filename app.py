from flask import Flask, render_template,request,redirect,session,flash,url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash

app=Flask(__name__)
app.config['SECRET_KEY']='dljfldjfldjfljnb'

# Database config
<<<<<<< HEAD
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://LpEGgtLxrN:gWW1MfFmp9@remotemysql.com/LpEGgtLxrN"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://uwvbwdehilvxvt:f96d60639aee6ca061637c0080fcfa295f9228cfe69754d1a7cc85eb7ebb7712@ec2-18-213-179-70.compute-1.amazonaws.com:5432/d2bal6alstn2ij"#heroku
=======
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://username:password@remotemysql.com/dbname"
>>>>>>> 3be20c5155a76ba5a60e793e7f483fe702cc9a54
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)

#Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True,nullable=False)
    password = db.Column(db.String(100),nullable=False)
    doc=db.relationship("Notes",backref="user")

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    message = db.Column(db.String(1000))
    imp=db.Column(db.String(2))
    username=db.Column(db.String(100),db.ForeignKey("user.name"))

@app.route("/",methods=["GET","POST"])
def first():
    # data=Notes.query.all() #not writing here as it will not update the content of data so better doing it after handling post.
    if "user" in session:
        user=session["user"]
        if request.method=="POST":
            res=request.form
            if "imp" in res.keys():
                imp="ye"
            else:
                imp="no"
            new=Notes(title=res["title"],message=res["message"],imp=imp,username=user)
            db.session.add(new)
            db.session.commit()
            # redirect("/")#it will only take us to the page instead updating the data variable
        data=Notes.query.filter_by(username=user)
        return render_template("index.html",data=data)
    else:
        return redirect("/login")

@app.route("/delete/<int:id>")
def delete(id):
    old=Notes.query.filter_by(id=id).first()
    db.session.delete(old)
    db.session.commit()
    return redirect("/")

@app.route("/login",methods=["GET","POST"])
def log():
    if request.method=="POST":
        req=request.form
        if req:
            name=req.get("name")
            password=req.get("password")
        user=User.query.filter_by(name=name).first()
        if user:
            if check_password_hash(user.password,password):
                session["user"]=user.name
                return redirect("/")
            else:
                flash("Password not matching")
        else:
            flash("Not Found")
    return render_template("login.html")


@app.route("/register",methods=["GET","POST"])
def reg():
    if request.method=="POST":
        req=request.form
        name=req.get("name")
        user=User.query.filter_by(name=name).first()
        if user:
            flash(f"User {user.name} already exists")
        else:
            password=req.get("password")
            password = generate_password_hash(password=password,method="sha256")
            new_user=User(name=name,password=password)
            db.session.add(new_user)
            db.session.commit()
            session["user"] = name
            return redirect("/")
    return render_template("login.html")


if __name__=="__main__":

    app.run(debug=True)
