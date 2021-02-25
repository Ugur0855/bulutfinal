from datetime import datetime
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask import abort, current_app, render_template, Flask, stream_with_context, request, Response, flash, render_template, redirect, url_for
from exam import Exam
from forms import ExamEditForm, LoginForm
from passlib.hash import pbkdf2_sha256 as hasher
from user import get_user

def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.data["username"]
        user = get_user(username)
        if user is not None:
            password = form.data["password"]
            if hasher.verify(password, user.password):
                login_user(user)
                flash("Login Succesfull :)")
                next_page = request.args.get("next", url_for("home_page"))
                return redirect(next_page)
        flash("Invalid credentials.")

    x = datetime.now()
    date = x.strftime("%x")
    day_name = x.strftime("%A")
    time = x.strftime("%X")
    return render_template("login.html", form=form, date = date, day_name = day_name, time = time)

def logout_page():
    logout_user()
    flash("Logged Out :(")
    return redirect(url_for("home_page"))

def home_page():
    x = datetime.now()
    date = x.strftime("%x")
    day_name = x.strftime("%A")
    time = x.strftime("%X")
    return render_template("home.html", date = date, day_name = day_name, time = time)

def exams_page():
    db = current_app.config["db"]
    if request.method == "GET":
        exams = db.get_exams()

        x = datetime.now()
        date = x.strftime("%x")
        day_name = x.strftime("%A")
        time = x.strftime("%X")
        return render_template("exams.html", exams=exams, date = date, day_name = day_name, time = time)
    else:
        if not current_user.is_admin:
            abort(401)
        form_exam_keys = request.form.getlist("exam_keys")
        for form_exam_key in form_exam_keys:
            db.delete_exam(int(form_exam_key))
        flash("%(num)d exams deleted." % {"num": len(form_exam_keys)})
        return redirect(url_for("exams_page"))

def exam_page(exam_key):
    db = current_app.config["db"]
    exam = db.get_exam(exam_key)
    if exam is None:
        abort(404)

    x = datetime.now()
    date = x.strftime("%x")
    day_name = x.strftime("%A")
    time = x.strftime("%X")
    return render_template("exam.html", exam=exam, date = date, day_name = day_name, time = time)

@login_required
def exam_add_page():
    if not current_user.is_admin:
        abort(401)
    form = ExamEditForm()
    if form.validate_on_submit():
        examname = form.data["examname"]
        numberofquestions = form.data["numberofquestions"]
        question = form.data["question"]
        a = form.data["a"]
        b = form.data["b"]
        c = form.data["c"]
        d = form.data["d"]
        e = form.data["e"]
        exam = Exam(examname, numberofquestions, question, a, b, c, d, e)
        db = current_app.config["db"]
        exam_key = db.add_exam(exam)
        flash("Exam added.")
        return redirect(url_for("exam_page", exam_key=exam_key))
    
    x = datetime.now()
    date = x.strftime("%x")
    day_name = x.strftime("%A")
    time = x.strftime("%X")
    return render_template("exam_edit.html", form=form, date = date, day_name = day_name, time = time)

@login_required
def exam_edit_page(exam_key):
    db = current_app.config["db"]
    exam = db.get_exam(exam_key)
    form = ExamEditForm()
    if form.validate_on_submit():
        examname = form.data["examname"]
        numberofquestions = form.data["numberofquestions"]
        question = form.data["question"]
        a = form.data["a"]
        b = form.data["b"]
        c = form.data["c"]
        d = form.data["d"]
        e = form.data["e"]
        exam = Exam(examname, numberofquestions, question, a, b, c, d, e)
        db.update_exam(exam_key, exam)
        flash("Exam updated.")
        return redirect(url_for("exam_page", exam_key=exam_key))
    form.examname.data = exam.examname
    form.numberofquestions.data = exam.numberofquestions
    form.question.data = exam.question
    form.a.data = exam.a
    form.b.data = exam.b
    form.c.data = exam.c
    form.d.data = exam.d
    form.e.data = exam.e

    x = datetime.now()
    date = x.strftime("%x")
    day_name = x.strftime("%A")
    time = x.strftime("%X")
    return render_template("exam_edit.html", form=form, date = date, day_name = day_name, time = time)

def validate_movie_form(form):
    form.data = {}
    form.errors = {}

    form_examname = form.get("examname", "").strip()
    if len(form_examname) == 0:
        form.errors["examname"] = "Title can not be blank."
    else:
        form.data["examname"] = form_examname

    form_numberofquestions = form.get("numberofquestions")
    if not form_numberofquestions:
        form.data["numberofquestions"] = None
    elif not form_numberofquestions.isdigit():
        form.errors["numberofquestions"] = "numberofquestions must consist of digits only."
    else:
        numberofquestions = int(form_numberofquestions)
        if (numberofquestions < 1) or (numberofquestions > 1):
            form.errors["numberofquestions"] = "numberofquestions can be only 1 for this system."
        else:
            form.data["numberofquestions"] = numberofquestions

    return len(form.errors) == 0