# coding=utf-8
""" User Center Application """

from flask import Blueprint


# User blueprint
bp_user = Blueprint('bp_user', __name__)


import views
