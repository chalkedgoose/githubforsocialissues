#!/usr/bin/env python
# -*- coding: utf-8 -*-

import falcon

class ApiIndex(object):

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.json = {
            "message": "Welcome to py-api 🎉!"
        }
