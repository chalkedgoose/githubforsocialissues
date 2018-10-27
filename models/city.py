#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from motorengine.document import Document
from motorengine.fields import StringField, DateTimeField

class City(Document):
    name: StringField(required=True)
    state: StringField(required=True)
    country: StringField(required=True)
