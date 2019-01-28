# -*- coding: utf-8 -*-
import sys
import json
from .. import db
from sqlalchemy import and_


class Translate(db.Model):
    trans_to = db.Column(db.Integer, db.ForeignKey('word.id'), primary_key=True)
    trans_from = db.Column(db.Integer, db.ForeignKey('word.id'), primary_key=True)

    def __repr__(self):
        return str(self.trans_to)

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(120), nullable=False)
    lang = db.Column(db.String(120), nullable=False)
    trans_to = db.relationship('Translate', backref='frm', primaryjoin=id==Translate.trans_to)
    trans_from = db.relationship('Translate', backref='to', primaryjoin=id==Translate.trans_from)

    def __repr__(self):
        return self.value + "_" + self.lang

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
        wib_1 = cls.word_in_base(word_1, lang_1)
        wib_2 = cls.word_in_base(word_2, lang_2)
        if wib_1 and wib_2:
            return json.dumps({
                'words': [
                    wib_1.get_param(),
                    wib_2.get_param()
                ],
                    'status': 'оба слова в базе'
            })
        elif wib_1:
            return json.dumps({
                'words': [
                    wib_1.get_param(),
                    cls.create_word_and_trans(word_2, lang_2, wib_1).get_param()
                    ],
                'status': 'в базу добавлено слово' + lang_2
            })
        elif wib_2:
            return json.dumps({
                'words': [
                    cls.create_word_and_trans(word_1, lang_1, wib_2).get_param(),
                    wib_2.get_param()
                    ],
                'status': 'в базу добавлено слово' + lang_1
            })
        else:
            pair = cls.create_pair(word_1, word_2, lang_1, lang_2)
            return json.dumps({
                'words': [
                    pair[0].get_param(),
                    pair[1].get_param()],
                'status': 'Добавлено оба слова'
            })

    @classmethod
    def word_in_base(cls, word, lang):
        return cls.query.filter(and_(cls.value == word, cls.lang == lang)).first()

    @classmethod
    def create_word_and_trans(cls, word, lang, translit):
        newWord = cls(value=word, lang=lang)
        db.session.add(newWord)
        trans_1 = Translate(to = translit, frm = newWord)
        trans_2 = Translate(to = newWord, frm = translit)
        db.session.add(trans_1)
        db.session.add(trans_2)
        db.session.commit()
        return newWord

    @classmethod
    def create_pair(cls, first, sec, first_l, sec_l):
        newRus = cls(value=first, lang=first_l)
        newEng = cls(value=sec, lang=sec_l)
        db.session.add(newRus)
        db.session.add(newEng)
        trans_1 = Translate(to = newRus, frm = newEng)
        db.session.add(trans_1)
        trans_2 = Translate(frm = newRus, to = newEng)
        db.session.add(trans_2)
        db.session.commit()
        return (newRus, newEng)

    @classmethod
    def get_all(cls, lang, trans_lang):
        all_word = cls.query.filter(cls.lang == lang).all()
        words_with_translate = []
        for word in all_word:
            trans_arr = []
            for trans_index in word.trans_from:
                trans = trans_index.frm
                if trans.lang == trans_lang:
                    trans_arr.append({
                    'id': trans.id,
                    'value': trans.value
                    })
            words_with_translate.append({
            'id': word.id,
            'value': word.value,
            'trans': trans_arr
            })
        return json.dumps(words_with_translate)
