from flask import Flask, request
from flask import render_template, redirect, url_for, make_response
from user.routes import user_blueprint
from order.routes import order_blueprint
import requests

app = Flask(__name__)
app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(order_blueprint, url_prefix='/order')
app.config['SECRET_KEY'] = 'SECRET_KEY'

@app.route("/")
def index():
    #a = requests.get('http://127.0.0.1:8000/api/ex/').json()
    return render_template('index.html')


@app.route("/repair", methods=["GET", "POST"])
def repair():
    a = requests.get('http://127.0.0.1:8000/order/api/order/').json()

    return render_template('repair.html', a=a)




if __name__ == '__main__':
    app.run(debug=True)
