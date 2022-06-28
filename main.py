from flask import Flask, request
from flask import render_template, redirect, url_for, make_response

app = Flask(__name__)




@app.route("/")
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)