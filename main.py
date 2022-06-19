from flask import Flask
import requests
from flask import render_template

app = Flask(__name__)
menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

@app.route("/")
def index():
    return render_template('base.html', title='Главная страница', menu=menu)


if __name__ == "__main__":
    app.run(debug=True)