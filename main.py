from flask import Flask, request
from flask import render_template, redirect, url_for, make_response
from user.routes import user_blueprint
from order.routes import order_blueprint
from contact.routes import contact_blueprint
from executor.routes import executor_blueprint
import requests
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(user_blueprint, url_prefix="/user")
app.register_blueprint(order_blueprint, url_prefix="/order")
app.register_blueprint(contact_blueprint, url_prefix="/contact")

app.register_blueprint(executor_blueprint, url_prefix="/executor")


@app.route("/")
def index():
    order = requests.get(f"{Config.API_URL}/order/api/order/").json()
    executor = requests.get(f"{Config.API_URL}/api/executor/").json()
    speciality = requests.get(f"{Config.API_URL}/api/speciality/").json()
    return render_template("index.html", order=order, executor=executor, speciality=speciality )



if __name__ == "__main__":
    app.run(debug=True)
