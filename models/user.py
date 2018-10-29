#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mongoengine import *


class Users(Document):
    avatar = StringField(required=True, default='')
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
    issues_resolved = ListField(ReferenceField('Issue'))
