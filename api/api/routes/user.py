# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import request
from ..models import User

user_api = Blueprint('user_api', __name__)

@user_api.route('/user/registrate', methods=['GET','POST'])
def word_add():
    """add word to db """
    if request.method == "POST":
        User.user_or_registrate(request)
        return 'ok'
