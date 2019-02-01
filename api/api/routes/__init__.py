# -*- coding: utf-8 -*-
from flask import  Flask, flash, request
from .. import app, db
from ..models import Word, User, Dictionary, Dictionary_word, Answer, Word_associate
from .word import word_api
from .user import user_api
from .dictionary import dictionary_api

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Word': Word,
        'User': User,
        'Dictionary': Dictionary,
        'Dictionary_word': Dictionary_word,
        'Answer': Answer,
        'Word_associate': Word_associate
    }

app.register_blueprint(word_api)
app.register_blueprint(user_api)
app.register_blueprint(dictionary_api)
