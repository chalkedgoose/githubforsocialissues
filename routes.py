#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from server import api
from controllers.api import ApiRoutes
from controllers.cities import CityRoutes

api.add_route('/', ApiRoutes())
api.add_route('/cities', CityRoutes())
