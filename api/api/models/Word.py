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
    trans_to = db.relationship('Word',
        secondary=Word_associate,
        primaryjoin=id==Word_associate.c.trans_to,
        secondaryjoin=id==Word_associate.c.trans_from,
        backref="trans_from")
    # trans_from = db.relationship('Word', secondary="word_associate",foreign_keys="Word_associate.trans_from", cascade="save-update, merge, delete")

    def __repr__(self):
        return str(self.id) + "_" + self.value + "_" + self.lang

    def get_param(self):
        elem = {}
        elem['id'] = self.id
        elem['lang'] = self.lang
        elem['value'] = self.value
        return elem

    @classmethod
    def create(cls, request):
        lang_1 = request.form['lang_1'].strip().lower()
        lang_2 = request.form['lang_2'].strip().lower()
        word_1 = request.form['word_1'].strip().lower()
        word_2 = request.form['word_2'].strip().lower()
        word_1 = cls.create_or_get_word(word_1, lang_1)
        word_2 = cls.create_or_get_word(word_2, lang_2)
        # print(word_1.trans_from)
        cls.make_associate(word_1, word_2)

    @classmethod
    def make_associate(cls, w1, w2):
        if w1 not in w2.trans_to:
            w1.trans_to.append(w2)
            w2.trans_to.append(w1)
            db.session.commit()

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

    # @classmethod
    # def get_all(cls, lang, trans_lang):
    #     all_word = cls.query.filter(cls.lang == lang).all()
    #     words_with_translate = []
    #     for word in all_word:
    #         trans_arr = []
    #         for trans_index in word.trans_from:
    #             trans = trans_index.trans_to
    #             if trans.lang == trans_lang:
    #                 trans_arr.append({
    #                 'id': trans.id,
    #                 'value': trans.value
    #                 })
    #         words_with_translate.append({
    #         'id': word.id,
    #         'value': word.value,
    #         'trans': trans_arr
    #         })
    #     return json.dumps(words_with_translate)
