#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import falcon
import falcon_jsonify
from mongoengine import *
from middlewares.error import ErrorHandler
from middlewares.request_tracker import RequestTracker

# Entry point for our API
api = falcon.API(middleware=[
    falcon_jsonify.Middleware(help_messages=True),  # show helpful messages
    ErrorHandler(),
    RequestTracker()

])

# Connect to mongodb
connect('githubforsocialissues')
