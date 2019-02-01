# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import request
from ..models import *

dictionary_api = Blueprint('dictionary_api', __name__)

@dictionary_api.route('/dictionary/new', methods=['GET','POST'])
def new_dict():
    """create new dict for user """
    if request.method == "POST":
        return Dictionary.new_dict(request)

@dictionary_api.route('/dictionary/get-all-dicts-name', methods=['GET','POST'])
def get_all_dicts_name():
    """create new dict for user """
    if request.method == "POST":
        return Dictionary.get_all_dicts_name(request)
