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

    def to_json(self):
        ''' Converts document to dictionary in json format '''
        return {
            "id": str(self.id),
            "title": self.title,
            "description": self.description,
            "author": str(self.author),
            "resolved_by": str(self.resolved_by),
            "city": str(self.city)
        }
