import pytest
import requests
from bson import ObjectId

endpoint = "https://153cb064.ngrok.io/cities"
payload = {"name": "San Jose", "state": "California", "country": "USA"}
putload = {"name": "Santa Clara", "state": "California", "country": "USA"}


def delete_cities(documentid, endpoint):
    id_payload = {"id": documentid}
    r = requests.delete(endpoint, json=id_payload)


def get_cities(endpoint):
    r = requests.get(endpoint)
    return r


def post_cities(endpoint, payload):
    r = requests.post(endpoint, json=payload)
    doc_obj = r.json()
    return doc_obj


def put_cities(endpoint, payload, id):
    pload = {"id": id, "name": payload['name'],
             "state": payload['state'], "country": payload['country']}
    r = requests.put(endpoint, pload)


def testCities():
    get_city = get_cities(endpoint)
    post_city = post_cities(endpoint, payload)
    city_id = post_city['id']
    put_city = put_cities(endpoint, putload, city_id)
    assert get_city.status_code == 200
    assert post_city['state'] == "California"
    assert put_city['city'] == "Santa Clara"

#     print(city_id)
#     delete_cities(city_id, endpoint)


testCities()
