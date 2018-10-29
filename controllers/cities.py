#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import falcon
from bson import ObjectId
from models.city import Cities as City


class CityRoutes(object):

    def on_get(self, req, resp):
        if 'id' in req.params and ObjectId.is_valid(req.params['id']):
            try:
                city = City.objects(id=req.params['id'])
                resp.json = City.to_json(city[0])
            except Exception:
                resp.status = falcon.HTTP_400
                resp.json = {
                    "message": "City id: %s not found in database!" %
                    req.params['id']
                }
        else:
            cities = [City.to_json(i) for i in City.objects]
            resp.json = cities

    def on_post(self, req, resp):
        try:
            city = City(
                name=req.get_json('name'),
                state=req.get_json('state'),
                country=req.get_json('country')
            )
            city.save()
            resp.json = City.to_json(city)
        except Exception as e:
            resp.status = falcon.HTTP_400
            if hasattr(e, 'title') and hasattr(e, 'description'):
                resp.json = {
                    "message": "%s - %s" % (e.title, e.description)
                }

    def on_put(self, req, resp):
        return

    def on_delete(self, req, resp):
        if 'id' in req.params and ObjectId.is_valid(req.params['id']):
            res = City.objects(id=req.params['id']).delete()
            if res == 1:
                resp.json = {
                    "message": "City id: %s deleted successfully!" %
                    req.params['id']
                }
            else:
                resp.status = falcon.HTTP_400
                resp.json = {
                    "message": "City id: %s not in database!" %
                    req.params['id']
                }
