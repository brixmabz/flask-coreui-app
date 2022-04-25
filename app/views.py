from functools import reduce
from flask import Blueprint, flash, render_template, redirect, request, url_for, jsonify
from flask_login import login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from jinja2 import TemplateNotFound

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def index():
    return render_template('home/index.html', title="Home", user=current_user)


@views.route('/<template>')
@login_required
def route_template(template):
    try:
        if not template.endswith('.html'):
            template += '.html'

        return render_template("home/" + template)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


@views.errorhandler(404)
def page_not_found():
    return render_template("home/page-404.html"), 404


@views.errorhandler(500)
def internal_server_error():
    return render_template("home/page-500.html"), 500
