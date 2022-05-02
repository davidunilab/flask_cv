from flask import Flask, render_template, request
from wtforms.validators import DataRequired

from data.database import edu, working
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, TextAreaField, IntegerField, StringField

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cv.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Work (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.String(20))
    finish = db.Column(db.String(20), nullable=True)
    position = db.Column(db.String(220),nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return '<Work %r>' % self.position



class Edu (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.String(20))
    finish = db.Column(db.String(20), nullable=True)
    curse = db.Column(db.String(220),nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return '<Edu %r>' % self.curse


class EduForm (Form):
    start = IntegerField("კურსის დაწყება", validators=[DataRequired("ველი სავალდებულოა")])
    finish = IntegerField("კურსის დამთავრება", validators=[DataRequired()])
    curse = StringField("კურსის სახელი", validators=[DataRequired()])
    description = TextAreaField("კურსის აღწერა")



@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    working = Work.query.all()
    edu = Edu.query.all()
    print(working)
    return render_template("about.html", education=edu, working=working)


@app.route("/work/add")
def work_add():
    work = Work(start="2023", finish="2024", position="Web Developer")
    db.session.add(work)
    db.session.commit()
    return "მონაცემი წარმატებით დაემატა"

@app.route("/work/edit/<int:id>")
def work_edit(id):
    work = Work.query.filter_by(id=id).first()
    work.position = "Fullstack web dev"
    db.session.add(work)
    db.session.commit()
    return "მონაცემი წარმატებით განახლდა"


@app.route("/work/delete/<int:id>")
def work_delete(id):
    work = Work.query.filter_by(id=id).first()
    db.session.delete(work)
    db.session.commit()
    return "მონაცემი წარმატებით წაიშალა"

@app.route("/gallery", methods = ["GET","POST"])
def gallery():
    form = EduForm()

    if request.method == 'POST' and form.validate():
        start = request.form["start"]
        finish = request.form["finish"]
        curse = request.form["curse"]
        description = request.form["description"]

        edu = Edu(start=start, finish=finish, curse=curse, description=description)
        db.session.add(edu)
        db.session.commit()

    edu = Edu.query.all()
    return render_template("gallery.html", edu=edu, form=form)


if __name__ == "__main__":
    app.run(debug=True)