#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import falcon
import falcon_jsonify

from mongoengine import *
from middlewares.error import ErrorHandler

api = falcon.API(middleware=[
    falcon_jsonify.Middleware(help_messages=True),  # show helpful messages
    ErrorHandler()
])

# connect to mongodb
connect('py-api')
