#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import falcon
from models.req import Reqs as Req


class RequestTracker:

    # Middleware activated after other routes send a response
    def process_response(self, req, resp, resource, req_succeeded):

        # If the response status is not 200 (Ok) and request is
        # is successful, create mvp document logging request
        if resp.status == falcon.HTTP_200 and req_succeeded:
            request = Req(
                method=req.method,
                endpoint=req.relative_uri,
                ip=req.remote_addr
            )
            request.save()
