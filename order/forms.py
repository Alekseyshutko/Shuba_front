from flask_wtf import FlaskForm
from wtforms import FileField, StringField, DateField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo


class OrderForm(FlaskForm):
    # user = StringField(
    #     "username",
    #     validators=[
    #         DataRequired(),
    #     ],
    # )
    title = StringField(
        "title",
        validators=[
            DataRequired(),
        ],
    )
    description = StringField(
        "description",
        validators=[
            DataRequired(),
        ],
    )
    city = StringField(
        "city",
        validators=[
            DataRequired(),
        ],
    )
    name = StringField(
        "name",
        validators=[
            DataRequired(),
        ],
    )
    phonenumber = StringField(
        "phone",
        validators=[
            DataRequired(),
        ],
    )
    photo = FileField(
        "photo",
        validators=[
            DataRequired(),
        ],
    )
    price = StringField(
        "price",
        validators=[
            DataRequired(),
        ],
    )
    date_finish = DateField("End Date", format='%Y-%m-%d')
    speciality = SelectField("специализация", choices=[1, 2])
    submit = SubmitField("Оставить заказ")


class CommentForm(FlaskForm):
    body = StringField("Ваш комментарий", validators=[
            DataRequired(),
        ],)
    submit = SubmitField("Оставить комментарий")