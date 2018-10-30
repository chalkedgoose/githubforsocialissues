#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from mongoengine import *
from mongoengine import Document


class Cities(Document):
    ''' City Class with Mongo Features '''
    name = StringField(required=True)
    state = StringField(required=True)
    country = StringField(required=True)

    def to_json(self):
        '''Converts document to dictionary in json format'''
        return {
            "id": str(self.id),
            "name": self.name,
            "state": self.state,
            "country": self.country
        }
