from flask import Flask, Blueprint
import os


def set_template_folder(blueprint, app, templates_subfolder=None):
    """ Set Blueprint template_folder to app's
        TEMPLATE_FOLDER/blueprint.name  """

    if not isinstance(blueprint, Blueprint):
        raise TypeError("blueprint must be a Blueprint.")

    if not isinstance(app, Flask):
        raise TypeError("app must be a Flask app.")

    if templates_subfolder is None:
        templates_subfolder = blueprint.name

    blueprint.template_folder = os.path.join(
        app.root_path, app.config['TEMPLATE_FOLDER'], templates_subfolder)
