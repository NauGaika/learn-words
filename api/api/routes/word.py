# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import request
from ..models import *
import json

word_api = Blueprint('word_api', __name__)

@word_api.route('/word/add', methods=['GET','POST'])
def word_add():
    """add word to db """
    if request.method == "POST":
        req = json.loads(request.data)
        if int(req['userId']):
            usr = User.user_verificateion(req['userId'])
            if usr:
                dictionary = usr.user_dict_id_is_exist(req['dictId'])
                if dictionary:
                    word = Word.create_or_get_word_by_value( req['word'], dictionary.lang)
                    translate = Word.create_or_get_word_by_value(req['translate'], dictionary.trans_lang)
                    if word and translate:
                        associate = word.add_translate_if_not_exits(translate)
                        dictionary.add_associate_if_no_exist(associate)
                        ret_data = {}
                        ret_data['associate_id'] = associate.id
                        ret_data['word'] = word.value
                        ret_data['translate'] = translate.value
                        return json.dumps(ret_data)
        # Word.create(request)
    return 'error'

@word_api.route('/word/get-all-from-dict/', methods=['GET','POST'])
def word_get_all_from_dict():
    """get all word """
    if request.method == "POST":
        req = json.loads(request.data)
        usr = User.user_verificateion(req['userId'])
        if usr:
            dict = usr.user_dict_id_is_exist(req['dictId'])
            if dict:
                obj_to_post = {
                    'words': dict.get_all_word_from_dict(),
                    'lang': dict.lang,
                    'trans_lang': dict.trans_lang
                }
                return json.dumps(obj_to_post)
    return ""


@word_api.route('/word/get-all/<langs>', methods=['GET','POST'])
def word_get_all(langs):
    """get all word """
    if request.method == "GET":
        langs = langs.split('-')
        return json.dumps([])


@word_api.route('/word/get-word-translates/', methods=['GET','POST'])
def word_get_translates():
    """get all word """
    if request.method == "POST":
        req = json.loads(request.data)
        word = Word.get_word_if_exist(req['word'], req['lang'])
        arr_post = []
        if word:
            arr_post = word.get_translate_values()
        print(arr_post)
        return json.dumps(arr_post)
