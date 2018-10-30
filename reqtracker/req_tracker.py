#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .models.req import Reqs as req


class ReqTracker():
    ''' creates an instance of ReqTracker'''

    def __init__(self):
        pass

    def save_request(self, form, endpoint):
        x_request = req(form=form, endpoint=endpoint)
        x_request.save()
