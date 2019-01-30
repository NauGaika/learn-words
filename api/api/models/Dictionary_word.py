# -*- coding: utf-8 -*-
from .. import db
from .Word import Word
from .Dictionary import Dictionary

class Dictionary_word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word_id = db.Column(db.Integer, db.ForeignKey('word.id'), primary_key=True)
    dict_id = db.Column(db.Integer, db.ForeignKey('dictionary.id'), primary_key=True)
    last_show = db.Column(db.DateTime)
    show_count = db.Column(db.Integer, nullable=False, default=0)
    correct = db.Column(db.Integer, default=0)
