from os import name
from flask import Flask, render_template,request,redirect,session
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY']='dljfldjfldjfljnb'

# Database config
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://LpEGgtLxrN:gWW1MfFmp9@remotemysql.com/LpEGgtLxrN"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
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
    if request.method=="POST":
        res=request.form
        if "imp" in res.keys():
            imp="ye"
        else:
            imp="no"
        new=Notes(title=res["title"],message=res["message"],imp=imp)
        db.session.add(new)
        db.session.commit()
        # redirect("/")#it will only take us to the page instead updating the data variable
    data=Notes.query.all()
    return render_template("index.html",data=data)

@app.route("/delete/<int:id>")
def delete(id):
    old=Notes.query.filter_by(id=id).first()
    db.session.delete(old)
    db.session.commit()
    return redirect("/")

@app.route("/login",methods=["GET","POST"])
def log():
    if request.method=="POST":
        return request.form
    return render_template("login.html")


@app.route("/register",methods=["GET","POST"])
def reg():
    if request.method=="POST":
        req=request.form
        name=req.get("name")
        password=req.get("password")
        new_user=User(name=name,password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect("/login")
    return render_template("login.html")


if __name__=="__main__":
    db.create_all()
    app.run(debug=True)
