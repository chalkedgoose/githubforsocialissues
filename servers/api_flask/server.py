#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from controllers.api import ApiController


app = Flask(__name__)

# routes below
app.add_url_rule('/', view_func=ApiController.as_view('api'))