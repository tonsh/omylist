# coding=utf-8
""" home application """

from flask import Blueprint


# home blueprint
bp_home = Blueprint('bp_home', __name__)


import views
