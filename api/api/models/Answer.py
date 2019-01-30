# -*- coding: utf-8 -*-
from .. import db

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word_id = db.Column(db.Integer, db.ForeignKey('word.id'), primary_key=True)
    translate_id = db.Column(db.Integer, db.ForeignKey('word.id'), primary_key=True)
    date_show = db.Column(db.DateTime)
    correct = db.Column(db.Boolean, default=False)
