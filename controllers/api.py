#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import falcon
from reqtracker import req_tracker
# ApiRoutes Router Class

Tracker = req_tracker.ReqTracker()


class ApiRoutes(object):

    # Index route '/'
    def on_get(self, req, resp):
        Tracker.save_request('GET', '/')
        resp.json = {
            "message": "Welcome to githubforsocialissues 🎉!"
        }
