from flask import Blueprint, render_template

blueprint = Blueprint('foo', __name__)


@blueprint.route('/', methods=['GET'])
def get():
    return render_template('index.html')
    #return "Hello, Foo!"
