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
    # a = requests.get('http://127.0.0.1:8000/api/ex/').json()
    return render_template("index.html")


@app.route("/repair", methods=["GET", "POST"])
def repair():
    filter_spec = request.args.get("speciality")
    if filter_spec:
        a = requests.get(f"{API}/order/api/order/?speciality={filter_spec}").json()
    else:
        a = requests.get(f"{API}/order/api/order/").json()
    b = requests.get(f"{API}/order/api/specialityorder/").json()

    return render_template("repair.html", a=a, b=b)


if __name__ == "__main__":
    app.run(debug=True)
