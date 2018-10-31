#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from server import api
from controllers.api import ApiRoutes
from controllers.cities import CityRoutes
from controllers.issues import IssueRoutes
from controllers.users import UserRoutes


# Register routes with API
api.add_route('/', ApiRoutes())
api.add_route('/cities', CityRoutes())
api.add_route('/issues', IssueRoutes())
api.add_route('/users', UserRoutes())

# see a city and it's users  /cities/:city-id/users
api.add_route('/cities/{id}/users', CityRoutes())
