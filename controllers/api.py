#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import falcon

class ApiRoutes(object):

    def on_get(self, req, resp):
        resp.json = {
            "message": "Welcome to githubforsocialissues 🎉!"
        }
