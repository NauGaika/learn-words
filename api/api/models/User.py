# -*- coding: utf-8 -*-
import json
from .. import db
from .Dictionary import Dictionary

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    dicts = db.relationship('Dictionary', backref='user', lazy=False)

    @classmethod
    def registrate(cls, name):
        new_user = cls(name=name)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @classmethod
    def get_user_by_name(cls, name):
        user = cls.query.filter_by(name=name).first()
        return user

    @classmethod
    def user_or_registrate(cls, request):
        name = request.form['name']
        if name:
            user = cls.get_user_by_name(name)
            if user:
                return user
            user = cls.registrate(name)
            return user

    def get_user_data(self):
        user = {}
        user['id'] = self.id
        user['name'] = self.name
        return json.dumps(user)

    def create_new_dict(self, dict_name):
        dict = Dictionary(name=dict_name)
        db.session.add(dict)
        self.dicts.append(dict)
        db.session.commit()

    def get_user_dict(self):
        return list(self.dicts)
