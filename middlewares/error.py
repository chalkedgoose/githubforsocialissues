#!/usr/bin/env python
# -*- coding: utf-8 -*-

import falcon

class ErrorHandler:
    def process_resource(self, req, resp, resource, params):
        if resp.status != falcon.HTTP_200:
            raise falcon.HTTPBadRequest("Bad request")

    def process_response(self, req, resp, resource):
        if resp.status != falcon.HTTP_200:
            resp.status = falcon.HTTP_404
            resp.json = {
                "message": "Not Found - %s %s" % (req.method, req.relative_uri)
            }
