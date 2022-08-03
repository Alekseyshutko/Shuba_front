from flask_wtf import FlaskForm
from wtforms import FileField, StringField, DateField, SubmitField, EmailField, SelectMultipleField
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

    phone_number = StringField(
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

    photo = FileField(
        "photo",

    )

    speciality = SelectMultipleField("специализация", choices=[('1', 'стройка'), ('2', 'уборка')])
    submit = SubmitField("Стать исполнителем")


class CommentForm(FlaskForm):
    body = StringField("Ваш комментарий", validators=[
        DataRequired(),
    ], )
    submit = SubmitField("Оставить комментарий")