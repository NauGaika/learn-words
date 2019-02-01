# -*- coding: utf-8 -*-
from .. import db

class Dictionary_word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word_associate_id = db.Column(db.Integer, db.ForeignKey('word_associate.id'))
    dict_id = db.Column(db.Integer, db.ForeignKey('dictionary.id'))
    last_show = db.Column(db.DateTime)
    show_count = db.Column(db.Integer, default=0)
    correct = db.Column(db.Integer, default=0)
