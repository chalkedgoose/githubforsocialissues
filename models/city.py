#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from mongoengine import *
from mongoengine import Document


class Cities(Document):
    ''' City Class with Mongo Features '''
    name = StringField(required=True)
    state = StringField(required=True)
    country = StringField(required=True)

    def to_json(query_object):
    ''' returns object as dict '''
    return {
        "id": str(query_object.id),
        "name": query_object.name,
        "state": query_object.state,
        "country": query_object.country
    }
