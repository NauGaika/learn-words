# -*- coding: utf-8 -*-
from .. import db
from .Word import Word
class Dictionary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lang = db.Column(db.String(3), nullable=False)
    name = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    words = db.relationship('Word', secondary='dictionary_word', lazy=False, backref=db.backref('dictionary', lazy=False))
