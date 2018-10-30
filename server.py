#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import falcon
import falcon_jsonify
from mongoengine import *
from middlewares.error import ErrorHandler


# Entry point for our API
api = falcon.API(middleware=[
    falcon_jsonify.Middleware(help_messages=True),  # show helpful messages
    ErrorHandler()
])

# Connect to mongodb
connect('githubforsocialissues')
