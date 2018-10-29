#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mongoengine import *


class Issues(Document):
    title = StringField(required=True)
    description = StringField(required=True)
    author = ReferenceField('User', reverse_delete_rule=mongoengine.PULL)
    resolved_by = ReferenceField('User', reverse_delete_rule=mongoengine.PULL)
