# -*- coding: utf-8 -*-
from .. import db

Word_associate = db.Table("Word_associate",
    db.Column("trans_to", db.Integer, db.ForeignKey("word.id"), primary_key=True),
    db.Column("trans_from", db.Integer, db.ForeignKey("word.id"), primary_key=True)
)
