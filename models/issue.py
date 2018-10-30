#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mongoengine import *
from models.user import Users as User
from models.city import Cities as City


class Issues(Document):
    ''' creates issue document '''
    title = StringField(required=True)
    description = StringField(required=True)
    author = ReferenceField(User)
    resolved_by = ReferenceField(User)
    city = ReferenceField(City)

    def to_json(query_object):
        ''' returns Issue as a dict '''
        return {
            "id": str(query_object.id),
            "title": query_object.title,
            "description": query_object.description,
            "author": str(query_object.author),
            "resolved_by": str(query_object.resolved_by),
            "city": str(query_object.city)
        }
