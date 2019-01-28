# -*- coding: utf-8 -*-
from flask import  Flask, flash, request
from .. import app, db
from ..models import *
from .word import word_api

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Word': Word.Word,
        'Translate': Word.Translate
    }

app.register_blueprint(word_api)
