#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import falcon
from bson import ObjectId
from models.user import Users as User


class UserRoutes(object):

    def on_get(self, req, resp):
        if 'id' in req.params and ObjectId.is_valid(req.params['id']):
            try:
                user = User.objects(id=req.params['id'])[0]
                resp.json = User.to_json(user)
            except Exception:
                resp.status = falcon.HTTP_400
                resp.json = {
                    "message": "User id: %s not found in database!" %
                    req.params['id']
                }
        else:
            users = [User.to_json(i) for i in User.objects]
            resp.json = users

    def on_post(self, req, resp):
        try:
            user = User(
                avatar=req.get_json('avatar'),
                first_name=req.get_json('first_name'),
                last_name=req.get_json('last_name'),
                email=req.get_json('email'),
                password=req.get_json('password')
            )
            user.save()
            resp.json = User.to_json(user)
        except Exception as e:
            resp.status = falcon.HTTP_400
            if hasattr(e, 'title') and hasattr(e, 'description'):
                resp.json = {
                    "message": "%s - %s" % (e.title, e.description)
                }

    def on_put(self, req, resp):
        if 'id' in req.params and ObjectId.is_valid(req.params['id']):
            try:
                user = User.objects(id=req.params['id'])[0]
                if hasattr(req, 'json') and 'avatar' in req.json:
                    user.avatar = req.get_json('avatar')
                if hasattr(req, 'json') and 'first_name' in req.json:
                    user.first_name = req.get_json('first_name')
                if hasattr(req, 'json') and 'last_name' in req.json:
                    user.last_name = req.get_json('last_name')
                if hasattr(req, 'json') and 'email' in req.json:
                    user.email = req.get_json('email')
                if hasattr(req, 'json') and 'password' in req.json:
                    user.password = req.get_json('password')
                user.save()
                resp.json = User.to_json(user)
            except Exception:
                resp.status = falcon.HTTP_400
                resp.json = {
                    "message": "User id: %s not found in database!" %
                    req.params['id']
                }

    def on_delete(self, req, resp):
        if 'id' in req.params and ObjectId.is_valid(req.params['id']):
            res = User.objects(id=req.params['id']).delete()
            if res == 1:
                resp.json = {
                    "message": "User id: %s deleted successfully!" %
                    req.params['id']
                }
            else:
                resp.status = falcon.HTTP_400
                resp.json = {
                    "message": "User id: %s not in database!" %
                    req.params['id']
                }
