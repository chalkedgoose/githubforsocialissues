#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import falcon
import time

class ErrorHandler:
    def process_response(self, req, resp, resource, req_succeeded):
        if resp.status != falcon.HTTP_200 and not hasattr(resp, 'json'):
            resp.status = falcon.HTTP_404
            resp.json = {
                "message": "Not Found - %s %s" % (req.method, req.relative_uri)
            }
        if not req_succeeded:
            resp.status = falcon.HTTP_429
            resp.json = {
                "message": "Too Many Requests!"
            }
            time.sleep(3)
