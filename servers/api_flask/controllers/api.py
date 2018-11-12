#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask.views import MethodView


class ApiController(MethodView):

    def get(self):
        return 'hello'