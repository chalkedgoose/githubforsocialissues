#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import falcon

class ErrorHandler:
    def process_response(self, req, resp, resource):
        if resp.status != falcon.HTTP_200 and not hasattr(resp, 'json'):
            resp.status = falcon.HTTP_404
            resp.json = {
                "message": "Not Found - %s %s" % (req.method, req.relative_uri)
            }
