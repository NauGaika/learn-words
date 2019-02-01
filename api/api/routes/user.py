# -*- coding: utf-8 -*-
from flask import Blueprint, send_from_directory, url_for
from flask import request
from ..models import User
from .. import app
import os
import json

# from google_speech import Speech

user_api = Blueprint('user_api', __name__)

@user_api.route('/user/registrate', methods=['GET','POST'])
def word_add():
    """add word to db """
    if request.method == "POST":
        usr = User.user_or_registrate(request)
        ret_data = {
            'user_name': usr.name,
            'user_id': usr.id
        }
        return json.dumps(ret_data)



# @user_api.route('/test-speech/<word>', methods=['GET','POST'])
# def test_speech(word):
#     text = word
#     lang = "ru"
#     speech = Speech(text, lang)
#     # speech.play()
#     dirname = ""
#     dirname = os.path.join('api/static', text + '.mp3')
#     speech.save(dirname)
#
#     return "<audio autoplay='autoplay' src='" + url_for('static', filename=text + '.mp3') + "'></audio>"
#
# @user_api.route('/mp3/<path:path>')
# def send_js(path):
#     return send_from_directory('', path)
