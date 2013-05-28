from flask import Blueprint

blueprint = Blueprint('bar', __name__)


@blueprint.route('/', methods=['GET'])
def get():
    return "Hello, Bar!"
