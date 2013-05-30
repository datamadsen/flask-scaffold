from flask import Blueprint, render_template, request, redirect, url_for
from application.forms.foo import FooForm
from application.models import Foo, session

blueprint = Blueprint('foo', __name__)


@blueprint.route('/', methods=['GET'])
def get():
    foos = Foo.query.all()
    form = FooForm()
    return render_template('index.html', form=form, foos=foos)


@blueprint.route('/', methods=['POST'])
def post():
    form = FooForm(request.form)
    if form.validate():
        foo = Foo()
        foo.title = form.title.data
        session.add(foo)
        session.commit()
    return redirect(url_for('foo.get'))
