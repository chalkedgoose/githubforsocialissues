#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mongoengine import *


class Issues(Document):
    title = StringField(required=True)
    description = StringField(required=True)
    author = ReferenceField('User', reverse_delete_rule=mongoengine.PULL)
    resolved_by = ReferenceField('User', reverse_delete_rule=mongoengine.PULL)

    def to_json(query_object):
        return {
            "id": str(query_object.id),
            "title": query_object.title,
            "description": query_object.description,
            "author": str(query_object.author),
            "resolved_by": str(query_object.resolved_by)
        }
