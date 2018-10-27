#!/usr/bin/env python
# -*- coding: utf-8 -*-

from server import api
from controllers.api import ApiIndex

api.add_route('/', ApiIndex())
