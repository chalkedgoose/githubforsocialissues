#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mongoengine import *


class Cities(Document):
    name = StringField(required=True)
    state = StringField(required=True)
    country = StringField(required=True)

    def to_json(q):
        return {
            "id": str(q.id),
            "name": q.name,
            "state": q.state,
            "country": q.country
        }
