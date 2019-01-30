# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import request
from ..models import *

word_api = Blueprint('word_api', __name__)

@word_api.route('/word/add', methods=['GET','POST'])
def word_add():
    """add word to db """
    if request.method == "POST":
        Word.create(request)
    return 'ok'

@word_api.route('/word/get-all/<langs>', methods=['GET','POST'])
def word_get_all(langs):
    """get all word """
    if request.method == "GET":
        langs = langs.split('-')
        return Word.get_all(langs[0], langs[1])
