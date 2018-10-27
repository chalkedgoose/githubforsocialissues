#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import uvloop
import falcon
import falcon_jsonify
from tornado import ioloop
from motorengine import connect
from middlewares.error import ErrorHandler

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

api = falcon.API(middleware=[
    falcon_jsonify.Middleware(help_messages=True),  # show helpful debug messages
    ErrorHandler()
])

connect("py-api", host="localhost", port=27017, io_loop=ioloop.IOLoop.instance())
