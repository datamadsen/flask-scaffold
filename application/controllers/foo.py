from flask import Blueprint

blueprint = Blueprint('foo', __name__)


@blueprint.route('/', methods=['GET'])
def get():
    return "Hello, Foo!"
