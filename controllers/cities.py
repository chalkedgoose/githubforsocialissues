#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import falcon
from tornado import ioloop
from models.city import City

io_loop = ioloop.IOLoop.instance()

class CityRoutes(object):

    def on_get(self, req, resp):
        def find_cities():
            cities = City.objects.find_all(callback=handle_cities_found)
        def handle_cities_found(result):
            rows = []
            for i in result:
                if i.name is None or i.state is None or i.country is None:
                    continue
                row = {
                    'name': i.name,
                    'state': i.state,
                    'country': i.country
                }
                rows.append(row)
            resp.json = rows
            io_loop.stop()
        io_loop.add_timeout(1, find_cities)
        io_loop.start()

    def on_post(self, req, resp):
        try:
            City.objects.create(
                name=req.get_json('name'),
                state=req.get_json('state'),
                country=req.get_json('country')
            )
        finally:
            resp.json = {
                "name": req.get_json('name'),
                "state": req.get_json('state'),
                "country": req.get_json('country')
            }
