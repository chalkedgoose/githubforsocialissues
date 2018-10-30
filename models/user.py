#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mongoengine import *


class Users(Document):
    avatar = StringField(required=True, default='')
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)

    def to_json(query_object):
        return {
            "id": str(query_object.id),
            "avatar": query_object.avatar,
            "first_name": query_object.first_name,
            "last_name": query_object.last_name,
            "email": query_object.email,
            "password": query_object.password
        }
