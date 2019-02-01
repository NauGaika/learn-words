# -*- coding: utf-8 -*-
from .. import db
from .User import User
from .Dictionary_word import Dictionary_word
import json

class Dictionary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lang = db.Column(db.String(3), nullable=False)
    trans_lang = db.Column(db.String(3), nullable=False)
    name = db.Column(db.String(100))
    description = db.Column(db.Text, default="")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", backref="dicts")
    words = db.relationship('Word_associate', secondary='dictionary_word')

    def add_associate_if_no_exist(self, associate):
        if associate not in self.words:
            self.words.append(associate)
            db.session.commit()

    def get_all_word_from_dict(self):
        words = {}
        for w_a in self.words:
            word_name = w_a.word.value
            if word_name not in words.keys():
                words[word_name] = []
            words[word_name].append({
                'translate': w_a.translate.value,
                'associate_id': w_a.id
            })
        return words


    @classmethod
    def new_dict(cls, request):
        obj = json.loads(request.data)
        dict_name = str(obj['dictName'])
        lang = str(obj['lang'])
        trans_lang = str(obj['transLang'])
        data = {'id': obj['userId']}
        if lang and trans_lang and dict_name:
            usr = User.user_verificateion(request)
            if usr:
                new_dict = cls.create_dict_if_not_exist_for_user(dict_name, usr, lang, trans_lang)
                if new_dict:
                    return json.dumps({
                        'id': new_dict.id,
                        'name': new_dict.name,
                        'description': new_dict.description
                    })
        return 'error'

    @classmethod
    def create_dict_if_not_exist_for_user(cls, name, user, lang, trans_lang):
        if cls.dict_is_exist_by_name_and_user(user, name, lang, trans_lang):
            new_dict = cls(name=name, lang=lang, trans_lang=trans_lang)
            user.dicts.append(new_dict)
            db.session.commit()
            return new_dict

    @classmethod
    def dict_is_exist_by_name_and_user(cls, user, name, lang, trans_lang):
        for dictionary in user.dicts:
            if dictionary.name == name and dictionary.lang == lang and dictionary.trans_lang == trans_lang:
                return False
        return True

    @classmethod
    def get_all_dicts_name(cls, request):
        usr = User.user_verificateion(request)
        array_post = []
        if usr:
            for i in usr.dicts:
                array_post.append({
                    'id': i.id,
                    'name': i.name,
                    'description': i.description
                })
        return json.dumps(array_post)
