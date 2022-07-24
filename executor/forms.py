from flask_wtf import FlaskForm
from wtforms import FileField, StringField, DateField, SubmitField, EmailField
from wtforms.validators import DataRequired, EqualTo


class ExecutorForm(FlaskForm):
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

    phone_number = EmailField(
        "Номер телефона",
        validators=[
            DataRequired(),
        ],
    )

    city = StringField(
        "город",
        validators=[
            DataRequired(),
        ],
    )

    speciality = StringField(
        "специальность",
        validators=[
            DataRequired(),
        ],
    )

    submit = SubmitField("Стать исполнителем")