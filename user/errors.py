from flask import redirect, render_template, request, flash, url_for, abort
from werkzeug.exceptions import HTTPException, Unauthorized, Forbidden
from app import app
from user.utils import refresh

# from user.permissions import login_required, profile_required


logger = app.logger
TOKEN_EXPIRED = "Token has expired"
NEED_PROFILE = "Need to create profile"


@app.errorhandler(400)
def handle_bad_request(e: HTTPException):
    logger.error(e)
    flash(e.description)
    return redirect(request.url)


@app.errorhandler(401)
def handle_unauthorized(e: Unauthorized):
    if e.description == TOKEN_EXPIRED:
        try:
            auth = refresh()
            auth.store_in_session()
            return redirect(request.url, code=307)
        except Unauthorized as e:
            logger.error(e)
            flash("Your session was expired")
    return redirect(url_for("auth.login"))


@app.errorhandler(403)
def handle_forbidden(e: Forbidden):
    if e.description == NEED_PROFILE:
        return redirect(url_for("users.profile_create"))
    flash(e.description)
    return redirect(url_for("home"))


@app.errorhandler(500)
def internal_error(error):
    return "500 error"
