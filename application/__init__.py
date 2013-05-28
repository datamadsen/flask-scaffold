from flask import Flask
from application.config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

from application.controllers import site, foo, bar
app.register_blueprint(site.blueprint, url_prefix='/')
app.register_blueprint(foo.blueprint, url_prefix='/foo')
app.register_blueprint(bar.blueprint, url_prefix='/bar')
