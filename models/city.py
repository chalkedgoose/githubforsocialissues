#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mongoengine import *


class Cities(Document):
    name = StringField(required=True)
    state = StringField(required=True)
    country = StringField(required=True)

    def to_json(query_object):
        return {
            "id": str(query_object.id),
            "name": query_object.name,
            "state": query_object.state,
            "country": query_object.country
        }
