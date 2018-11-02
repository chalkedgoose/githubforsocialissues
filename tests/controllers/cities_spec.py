from pocha import it, describe, after
from falcon import testing
from routes import api
from models.city import Cities as City


client = testing.TestClient(api)

@after
def delete_test_cities():
    res = City.objects(name='testCity').delete()

@describe('Cities')
def api_tests():
    @it('should return json response for /cities GET')
    def cities_get_all():
        req = client.simulate_get('/cities')
        assert hasattr(req, 'json')
        assert req.status_code == 200

    @it('should return json response for /cities/id= GET')
    def cities_get_one():
        testCity = create_test_city()
        req = client.simulate_get('/cities', query_string='id=' + str(testCity.id))
        assert hasattr(req, 'json')
        assert req.json['name'] == 'testCity'
        assert req.status_code == 200
    def create_test_city():
        city = City(
                name="testCity",
                state="test",
                country="test"
            )
        city.save()
        return city