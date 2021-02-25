from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, NumberRange, Optional
from wtforms_components import IntegerField

from datetime import datetime

#examno, examname, numberofquestions, question, a, b, c, d, e
class ExamEditForm(FlaskForm):

    examname = StringField("Examname", validators=[DataRequired()])
    question = StringField("Question", validators=[DataRequired()])
    a = StringField("a", validators=[DataRequired()])
    b = StringField("b", validators=[DataRequired()])
    c = StringField("c", validators=[DataRequired()])
    d = StringField("d", validators=[DataRequired()])
    e = StringField("e", validators=[DataRequired()])

    numberofquestions = IntegerField(
        "Numberofquestions",
        validators=[
            Optional(),
            NumberRange(min=1, max=10),
        ],
    )

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])