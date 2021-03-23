from flask import Blueprint

bp = Blueprint('example_blueprint', __name__)

@bp.route('/')
def index():
    return "Hello World!"