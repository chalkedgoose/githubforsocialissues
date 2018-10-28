#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import falcon
from bson import ObjectId
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
                    'id': str(i._id),
                    'name': i.name,
                    'state': i.state,
                    'country': i.country
                }
                rows.append(row)
            resp.json = rows
            io_loop.stop()
        def find_city():
            if 'id' not in req.params:
                resp.status = falcon.HTTP_400
                io_loop.stop()
                return
            if not ObjectId.is_valid(req.params['id']):
                resp.status = falcon.HTTP_400
                io_loop.stop()
                return
            try:
                City.objects.get(
                    req.params['id'],
                    callback=handle_city_found
                )
            except Exception as e:
                resp.status = falcon.HTTP_400
                if hasattr(e, 'title') and hasattr(e, 'description'):
                    resp.json = {
                        "message": "%s - %s" % (e.title, e.description)
                    }
                io_loop.stop()
        def handle_city_found(result):
            resp.json = {
                "name": result._name,
                "state": result._state,
                "country": result._country
            }
            io_loop.stop()
        if req.params == {}:
            io_loop.add_timeout(1, find_cities)
        else:
            io_loop.add_timeout(1, find_city)
        io_loop.start()

    def on_post(self, req, resp):
        def create_city():
            try:
                City.objects.create(
                    name=req.get_json('name'),
                    state=req.get_json('state'),
                    country=req.get_json('country'),
                    callback=handle_city_created
                )
            except Exception as e:
                resp.status = falcon.HTTP_400
                if hasattr(e, 'title') and hasattr(e, 'description'):
                    resp.json = {
                        "message": "%s - %s" % (e.title, e.description)
                    }
                io_loop.stop()
        def handle_city_created(result):
            resp.json = {
                "name": result.name,
                "state": result.state,
                "country": result.country
            }
            io_loop.stop()
        io_loop.add_timeout(1, create_city)
        io_loop.start()

    def on_put(self, req, resp):
        def find_city():
            if 'id' not in req.params:
                resp.status = falcon.HTTP_400
                io_loop.stop()
                return
            if not ObjectId.is_valid(req.params['id']):
                resp.status = falcon.HTTP_400
                io_loop.stop()
                return
            try:
                City.objects.get(
                    req.params['id'],
                    callback=handle_city_found
                )
            except Exception as e:
                resp.status = falcon.HTTP_400
                if hasattr(e, 'title') and hasattr(e, 'description'):
                    resp.json = {
                        "message": "%s - %s" % (e.title, e.description)
                    }
                io_loop.stop()
        def handle_city_found(result):
            resp.json = {
                "name": result._name,
                "state": result._state,
                "country": result._country
            }
            io_loop.stop()
        io_loop.add_timeout(1, find_city)
        io_loop.start()
