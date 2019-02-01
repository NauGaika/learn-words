# -*- coding: utf-8 -*-
from .. import db
from sqlalchemy import and_
class Word_associate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word_id = db.Column(db.Integer, db.ForeignKey('word.id'))
    translate_id = db.Column(db.Integer, db.ForeignKey('word.id'))
    word = db.relationship("Word", primaryjoin="Word_associate.word_id == Word.id", backref="word_associates")
    translate = db.relationship("Word", primaryjoin="Word_associate.translate_id == Word.id")

    def __repr__(self):
        return '\n\rWord_associate id=' + str(self.id) + "\n\rword=" + self.word.value + "\n\rtranslate=" + self.translate.value + "\n\r"

    @classmethod
    def get_associate(cls, word, translate):
        return cls.query.filter(and_(cls.word==word, cls.translate == translate)).first()
