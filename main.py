from flask import Flask, request
from flask import render_template, redirect, url_for, make_response
from user.routes import user_blueprint
from order.routes import order_blueprint
import requests
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(user_blueprint, url_prefix="/user")
app.register_blueprint(order_blueprint, url_prefix="/order")
API = "http://127.0.0.1:8000"


@app.route("/")
def index():
    order = requests.get(f"{API}/order/api/order/").json()
    executor = requests.get(f"{API}/api/executor/").json()
    speciality = requests.get(f"{API}/api/speciality/").json()
    return render_template("index.html", order=order, executor=executor, speciality=speciality )


if __name__ == "__main__":
    app.run(debug=True)
