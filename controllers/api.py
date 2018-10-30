#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import falcon


# ApiRoutes Router Class
class ApiRoutes(object):

    # Index route '/'
    def on_get(self, req, resp):
        resp.json = {
            "message": "Welcome to githubforsocialissues 🎉!"
        }
