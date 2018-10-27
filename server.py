#!/usr/bin/env python
# -*- coding: utf-8 -*-

import falcon
import falcon_jsonify
import mongoengine as mongo
from middlewares.error import ErrorHandler


api = falcon.API(middleware=[
    falcon_jsonify.Middleware(help_messages=True),  # show helpful debug messages
    ErrorHandler()
])

mongo.connect(
    db='py-api',
    host='mongodb://localhost'
)
