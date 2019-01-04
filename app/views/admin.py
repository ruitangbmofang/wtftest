from flask import Blueprint

admin = Blueprint('admin', __name__)

@admin.route('/index/')
def index():
    return "this is admin's homepage"

