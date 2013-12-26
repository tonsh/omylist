# coding=utf-8
""" oauth application """

from flask import Blueprint


# sina blueprint
bp_sina = Blueprint('bp_sina', __name__)

# douban blueprint
bp_douban = Blueprint('bp_douban', __name__)

import sina
import douban
