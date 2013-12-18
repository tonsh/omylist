# coding=utf-8
""" user views """

from flask import Blueprint


# User blueprint
bp_user = Blueprint('bp_user', 'user')


@bp_user.route('/')
def index():
    return 'Hello World!'
