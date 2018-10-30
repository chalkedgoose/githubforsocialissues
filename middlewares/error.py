#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import falcon


class ErrorHandler:

    # Middleware activated after other routes send a response
    def process_response(self, req, resp, resource, req_succeeded):

        # If the response status is not 200 (Ok) and there is no json
        # in the response, send Not Found json error message
        if resp.status != falcon.HTTP_200 and not hasattr(resp, 'json'):
            resp.status = falcon.HTTP_404
            resp.json = {
                "message": "Not Found - %s %s" % (req.method, req.relative_uri)
            }
