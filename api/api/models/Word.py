# -*- coding: utf-8 -*-
import sys
import json
from .. import db
from .Word_associate import Word_associate
from sqlalchemy import and_

class Word(db.Model):
    __tablename__ = "word"
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(120), nullable=False)
    lang = db.Column(db.String(120), nullable=False)
    translates = db.relationship("Word",
        secondary="word_associate",
        backref="words",
        primaryjoin="Word.id==Word_associate.word_id",
        secondaryjoin="Word.id==Word_associate.translate_id")
    # word_associates = db.relationship("Word_associate", backref="word", primaryjoin="Word.id = Word_associate.word_id")

    def __init__(self, value, lang):
        self.value = value
        self.lang = lang

    def __repr__(self):
        return str(self.id) + "_" + self.value + "_" + self.lang

    def get_param(self):
        elem = {}
        elem['id'] = self.id
        elem['lang'] = self.lang
        elem['value'] = self.value
        return elem

    def add_translate_if_not_exits(self, word):
        if word not in self.translates:
            self.translates.append(word)
            db.session.commit()
        return Word_associate.get_associate(self, word)

    def get_translate_values(self):
        data_post = []
        k = 0
        for i in self.translates:
            data_post.append(i.value)
            if k > 9:
                break
            k = k + 1
        return data_post

    @classmethod
    def make_associate(cls, w1, w2):
        if w1 not in w2.trans_to:
            w1.trans_to.append(w2)
            w2.trans_to.append(w1)
            db.session.commit()



    @staticmethod
    def clear_string(string):
        return str(string).strip().lower()

    @classmethod
    def create_or_get_word_by_value(cls, word, lang):
        word = cls.clear_string(word)
        lang = cls.clear_string(lang)
        word = cls.create_or_get_word(word, lang)
        return word

    @classmethod
    def get_word_if_exist(cls, word, lang):
        word = cls.clear_string(word)
        lang = cls.clear_string(lang)
        word = cls.query.filter(and_(cls.value == word, cls.lang == lang)).first()
        return word


    @classmethod
    def create_or_get_word(cls, word, lang):
        word_in_base = cls.query.filter(and_(cls.value == word, cls.lang == lang)).first()
        if not word_in_base:
            word_in_base = cls.create_word(word, lang)
        return word_in_base

    @classmethod
    def create_word(cls, word, lang):
        new_word = cls(value=word, lang=lang)
        db.session.add(new_word)
        db.session.commit()
        return new_word
