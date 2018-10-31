#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import falcon
from bson import ObjectId
from models.city import Cities as City
from models.user import Users as User


# CityRoutes Router Class
class CityRoutes(object):

   # '/cities' GET
   # ? id parameter returns single matching document
   # ? all other or no parameters returns all documents in collection
   # > No request body required
   # = returns json collection of documents or
   # = single document representation in json
    def on_get(self, req, resp, **args):
        ''' City Controller Get Request Method '''
        
        # Returns users with specified city id
        if 'id' in args and ObjectId.is_valid(args['id']):
            resp.json = [i.to_json() for i in User.objects(city=args['id'])]

        # If ?id= is in url and value for id is valid ObjectId
        if 'id' in req.params and ObjectId.is_valid(req.params['id']):
            try:

                # Get document from db with specified id and respond in json
                resp.json = City.objects(id=req.params['id'])[0].to_json()

            # Id not in database? - display error
            except Exception:
                resp.status = falcon.HTTP_400
                resp.json = {
                    "message": "City id: %s not found in database!" %
                    req.params['id']
                }

        # Everything else just display all cities
        else:
            cities = [i.to_json() for i in City.objects]
            resp.json = cities

    # '/cities' POST
    # ? No parameters
    # > All of the following in valid JSON format
    # > required: name, state, country
    # = returns json representation of new document
    def on_post(self, req, resp):
        ''' City Controller Post Request Method '''

        try:

            # Create document from json post data
            city = City(
                name=req.get_json('name'),
                state=req.get_json('state'),
                country=req.get_json('country')
            )

            # Save document to database
            city.save()

            # Respond with new document in json format
            resp.json = city.to_json()

        # Unable to create document? - return error as json
        except Exception as e:
            resp.status = falcon.HTTP_400
            if hasattr(e, 'title') and hasattr(e, 'description'):
                resp.json = {
                    "message": "%s - %s" % (e.title, e.description)
                }

    # '/cities' PUT
    # ? id parameter required
    # > At least one of the following in valid
    # > JSON format required: name, state, country
    # = returns json representation of updated document
    def on_put(self, req, resp):
        ''' City Controller Put Request Method '''

        # If ?id= is in url and value for id is valid ObjectId
        if 'id' in req.params and ObjectId.is_valid(req.params['id']):
            try:

                # Get document from db with specified id
                city = City.objects(id=req.params['id'])[0]

                # If req body has field, set found document
                # field to req body field
                if hasattr(req, 'json') and 'name' in req.json:
                    city.name = req.get_json('name')
                if hasattr(req, 'json') and 'state' in req.json:
                    city.state = req.get_json('state')
                if hasattr(req, 'json') and 'country' in req.json:
                    city.country = req.get_json('country')

                # Save document to database
                city.save()

                # Respond with updated document in json format
                resp.json = city.to_json()

            # Id not found in db? - return error in json format
            except Exception:
                resp.status = falcon.HTTP_400
                resp.json = {
                    "message": "City id: %s not found in database!" %
                    req.params['id']
                }

    # '/cities' DELETE
    # ? id parameter required
    # > No request body required
    # = returns json message
    def on_delete(self, req, resp):
        ''' City Controller Delete Request Method '''

        # If ?id= is in url and value for id is valid ObjectId
        if 'id' in req.params and ObjectId.is_valid(req.params['id']):

            # Find document by Id and delete it
            res = City.objects(id=req.params['id']).delete()

            # If document was deleted, send success message
            # in json - otherwise send error message
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
