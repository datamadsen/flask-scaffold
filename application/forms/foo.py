from application.models import Foo
from wtforms_alchemy import ModelForm

class FooForm(ModelForm):
    class Meta:
        model = Foo
