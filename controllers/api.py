#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import falcon

class ApiRoutes(object):

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.json = {
            "message": "Welcome to py-api 🎉!"
        }
