"""Add your views here.

We have started you with an initial blueprint. Add more as needed.
"""

from flask import Blueprint, flash


{{cookiecutter.app_name}} = Blueprint("{{cookiecutter.app_name}}", __name__)


@{{cookiecutter.app_name}}.route("/")
def index():
    return "Hello, world!"


def flash_errors(form, category="warning"):
    '''Flash all errors for a form.'''
    for field, errors in form.errors.items():
        for error in errors:
            flash("{0} - {1}"
                    .format(getattr(form, field).label.text, error), category)

