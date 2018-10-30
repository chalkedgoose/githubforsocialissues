#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mongoengine import *
from models.city import Cities as City


class Users(Document):
    ''' creates user  document '''
    avatar = StringField(required=True, default='')
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
    city = ReferenceField(City)

    def to_json(self):
        ''' Converts document to dictionary in json format '''
        return {
            "id": str(self.id),
            "avatar": self.avatar,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password
        }
