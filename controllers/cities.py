#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import falcon
from falconratelimit import rate_limit
from bson import ObjectId
from tornado import ioloop
from models.city import City

io_loop = ioloop.IOLoop.instance()

@falcon.before(rate_limit(per_second=2, window_size=2))
class CityRoutes(object):

    def on_get(self, req, resp):
        def find_cities():
            cities = City.objects.find_all(callback=handle_cities_found)
        def handle_cities_found(result):
            rows = []
            for i in result:
                if i.name is None or i.state is None or i.country is None:
                    continue
                id = str(i._id)
                row = {
                    'id': id,
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
            if result is None:
                resp.status = falcon.HTTP_400
                io_loop.stop()
                return
            id = str(result._id)
            resp.json = {
                "id": id,
                "name": result._name,
                "state": result._state,
                "country": result._country
            }
            io_loop.stop()
        if req.params == {}:
            io_loop.add_timeout(1, find_cities)
            io_loop.start()
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
            id = str(result._id)
            resp.json = {
                "id": id,
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
            if result is None:
                resp.status = falcon.HTTP_400
                io_loop.stop()
                return
            if not hasattr(req, 'json'):
                resp.status = falcon.HTTP_400
                resp.json = {
                    "message": "Request body is not valid JSON"
                }
                io_loop.stop()
                return
            if 'name' in req.json:
                result.name = req.json['name']
            if 'state' in req.json:
                result.state = req.json['state']
            if 'country' in req.json:
                result.name = req.json['country']
            result.save(callback=handle_city_updated)
        def handle_city_updated(result):
            name = result._name if 'name' not in req.json else req.json['name']
            state = result._state if 'state' not in req.json else req.json['state']
            country = result._country if 'country' not in req.json else req.json['country']
            id = str(result._id)
            resp.json = {
                "id": id,
                "name": name,
                "state": state,
                "country": country
            }
            io_loop.stop()
        io_loop.add_timeout(1, find_city)
        io_loop.start()
    def on_delete(self, req, resp):
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
            if result is None:
                resp.status = falcon.HTTP_400
                io_loop.stop()
                return
            result.delete(callback=handle_city_deleted)
        def handle_city_deleted(result):
            try:
                assert result == 1, \
                    "Unable to delete id: %s" % req.params['id']
            finally:
                resp.json = {
                    "message": "Deleted successfully id: %s" % req.params['id']
                }
                io_loop.stop()
        io_loop.add_timeout(1, find_city)
        io_loop.start()
