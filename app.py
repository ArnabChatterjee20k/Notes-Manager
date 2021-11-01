from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://LpEGgtLxrN:gWW1MfFmp9@remotemysql.com/LpEGgtLxrN"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)
class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    message = db.Column(db.String(120))
    imp=db.Column(db.String(2))

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
if __name__=="__main__":
    app.run(debug=True)
