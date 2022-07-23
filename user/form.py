from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, EqualTo


class RegisterUserForm(FlaskForm):

    email = EmailField(
        "Email",
        validators=[
            DataRequired(),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
        ],
    )
    password_submit = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            EqualTo("password"),
        ],
    )
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField(
        "email",
        validators=[
            DataRequired(),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
        ],
    )
    submit = SubmitField("Sign In")
