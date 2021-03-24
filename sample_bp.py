from flask import Blueprint

bp = Blueprint('bp', __name__, url_prefix="/admin", static_folder="static", template_folder="templates")

@bp.route('/')
def index():
    return "Hello World!"

@bp.route('/test')
def test():
    return "<h1>Test<h1>"