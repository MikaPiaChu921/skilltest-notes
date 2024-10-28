from flask import Flask, render_template, request, redirect, url_for, flash
from dbhelper import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '!@#$%^'

@app.route('/')
def createuser()->None:
    #doprocess("create table `student`(idno varchar(20), lastname varchar(20), firstname varchar(20), course varchar(20), level varchar(3))")
    #addrecord("student", idno="1", lastname="abellana", firstname="pia",course="bsit",level="4")
    # get all students
    head:list = ['idno','lastname','firstname','course','level']
    
    return render_template(
        "Index.html",title="create user", studentlist = getall("student")
    )

@app.route("/savestudent", methods=['POST', 'GET'])
def savestudent()->None:

    idno = request.form["idno"]
    lastname = request.form["lastname"]
    firstname = request.form["firstname"]
    course = request.form["course"]
    level = request.form["level"]

    addrecord("student", idno=idno, lastname=lastname, firstname=firstname,course=course,level=level)
    return redirect("/")

@app.route("/delete/<idno>", methods=['POST', 'GET'])
def deletestudent(idno)->None:
    deleterecord("student", idno=idno)

    return redirect("/")

@app.route("/update/<idno>", methods=['POST', 'GET'])
def updatestudent(idno)->None:

    studentdata = None

    studentlist = getall("student")
    for student in studentlist:
        if idno == student["idno"]:
            studentdata = student

    return render_template("/editstudent.html", student=studentdata)

@app.route("/updatestudent", methods=['POST', 'GET'])
def Astudent()->None:

    idno = request.form["idno"]
    lastname = request.form["lastname"]
    firstname = request.form["firstname"]
    course = request.form["course"]
    level = request.form["level"]

    editrecord("student", idno=idno, lastname=lastname, firstname=firstname,course=course,level=level)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)