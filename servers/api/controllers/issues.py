#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import falcon
from bson import ObjectId
from models.issue import Issues as Issue


class IssueRoutes(object):

    def on_get(self, req, resp):
        ''' Issues Controller Get Request Method '''

        if 'id' in req.params and ObjectId.is_valid(req.params['id']):
            try:
                resp.json = Issue.objects(id=req.params['id'])[0].to_json()
            except Exception:
                resp.status = falcon.HTTP_400
                resp.json = {
                    "message": "Issue id: %s not found in database!" %
                    req.params['id']
                }
        else:
            issues = [i.to_json() for i in Issue.objects]
            resp.json = issues

    def on_post(self, req, resp):
        ''' Issues Controller Post Request Method '''

        try:
            issue = Issue(
                title=req.get_json('title'),
                description=req.get_json('description'),
                author=ObjectId(req.get_json('author')),
                resolved_by=ObjectId(req.get_json('resolved_by'))
            )
            issue.save()
            resp.json = issue.to_json()
        except Exception as e:
            resp.status = falcon.HTTP_400
            if hasattr(e, 'title') and hasattr(e, 'description'):
                resp.json = {
                    "message": "%s - %s" % (e.title, e.description)
                }

    def on_put(self, req, resp):
        ''' Issues Controller Put Request Method '''

        if 'id' in req.params and ObjectId.is_valid(req.params['id']):
            try:
                issue = Issue.objects(id=req.params['id'])[0]
                if hasattr(req, 'json') and 'title' in req.json:
                    issue.title = req.get_json('title')
                if hasattr(req, 'json') and 'description' in req.json:
                    issue.description = req.get_json('description')
                if hasattr(req, 'json') and 'author' in req.json:
                    issue.author = ObjectId(req.get_json('author'))
                if hasattr(req, 'json') and 'resolved_by' in req.json:
                    issue.resolved_by = ObjectId(req.get_json('resolved_by'))
                issue.save()
                resp.json = issue.to_json()
            except Exception:
                resp.status = falcon.HTTP_400
                resp.json = {
                    "message": "Issue id: %s not found in database!" %
                    req.params['id']
                }

    def on_delete(self, req, resp):
        ''' Issues Controller Delete Request Method '''

        if 'id' in req.params and ObjectId.is_valid(req.params['id']):
            res = Issue.objects(id=req.params['id']).delete()
            if res == 1:
                resp.json = {
                    "message": "Issue id: %s deleted successfully!" %
                    req.params['id']
                }
            else:
                resp.status = falcon.HTTP_400
                resp.json = {
                    "message": "Issue id: %s not in database!" %
                    req.params['id']
                }
