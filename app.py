from flask import Flask, request
from flask import render_template, redirect, url_for, make_response
from user.routes import user_blueprint
from order.routes import order_blueprint
from contact.routes import contact_blueprint
from executor.routes import executor_blueprint
import requests
from config import Config
import errors

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(user_blueprint, url_prefix="/user")
app.register_blueprint(order_blueprint, url_prefix="/order")
app.register_blueprint(contact_blueprint, url_prefix="/contact")
app.register_blueprint(executor_blueprint, url_prefix="/executor")
app.config["SECRET_KEY"] = "12345678"


@app.route("/")
def index():
    order = requests.get(f"{Config.API_URL}/order/api/order/").json()
    executor = requests.get(f"{Config.API_URL}/api/executor/").json()
    speciality = requests.get(f"{Config.API_URL}/api/speciality/").json()
    return render_template("index.html", order=order, executor=executor, speciality=speciality)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
