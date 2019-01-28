# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import request
from ..models import *

word_api = Blueprint('word_api', __name__)

@word_api.route('/word/add', methods=['GET','POST'])
def word_add():
    """add word to db """
    if request.method == "POST":
        return Word.Word.create(request)
    return ''

@word_api.route('/word/get-all', methods=['GET','POST'])
def word_get_all():
    """get all word """
    if request.method == "GET":
        return Word.Word.get_all('en', 'ru')
