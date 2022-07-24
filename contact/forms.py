from flask_wtf import FlaskForm
from wtforms import FileField, StringField, DateField, SubmitField, EmailField
from wtforms.validators import DataRequired, EqualTo


class ContactForm(FlaskForm):
    first_name = StringField(
        "title",
        validators=[
            DataRequired(),
        ],
    )

    last_name = StringField(
        "title",
        validators=[
            DataRequired(),
        ],
    )

    email = EmailField(
        "Email",
        validators=[
            DataRequired(),
        ],
    )

    message = StringField(
        "description",
        validators=[
            DataRequired(),
        ],
    )

    submit = SubmitField("Отправить сообщение")