from flask import Flask, request
from flask import render_template, redirect, url_for, make_response
from user.routes import user_blueprint

app = Flask(__name__)
app.register_blueprint(user_blueprint, url_prefix='/user')
app.config['SECRET_KEY'] = 'SECRET_KEY'

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
