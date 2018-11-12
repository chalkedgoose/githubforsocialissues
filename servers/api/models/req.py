#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from mongoengine import *
from datetime import datetime


class Reqs(Document):
    ''' Creates request instance '''

    method = StringField(required=True)
    endpoint = StringField(required=True)
    ip = StringField()
    accessed_on = DateTimeField(default=datetime.now)


    def to_json(self):
        ''' returns document as json '''
        return {
            "method": str(self.form),
            "endpoint": str(self.endpoint),
            "called_on": str(self.called_on)
        }
