#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from server import api
from controllers.api import ApiRoutes
from controllers.cities import CityRoutes
from controllers.issues import IssueRoutes

api.add_route('/', ApiRoutes())
api.add_route('/cities', CityRoutes())
api.add_route('/issues', IssueRoutes())
