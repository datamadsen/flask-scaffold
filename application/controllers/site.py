from flask import Blueprint

blueprint = Blueprint('site', __name__)


@blueprint.route('/', methods=['GET'])
def get():
    return "Hello, World!"
