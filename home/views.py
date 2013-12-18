# coding=utf-8

from flask import Blueprint


# home blueprint
bp_home = Blueprint('bp_home', 'home')


@bp_home.route('/')
def index():
    return 'Hello World!!'
