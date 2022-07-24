from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField, EmailField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    first_name = StringField(
        "Имя",
        validators=[
            DataRequired(),
        ],
    )

    last_name = StringField(
        "Фамилия",
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


