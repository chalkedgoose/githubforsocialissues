from pocha import it, describe
from falcon import testing
from routes import api

client = testing.TestClient(api)

@describe('API')
def api_tests():
    @it('should return json response for / GET')
    def index():
        req = client.simulate_get('/')
        assert hasattr(req, 'json')
        assert req.status_code == 200

    @it('should return json error for /invalidpath GET')
    def index():
        req = client.simulate_get('/invalidpath')
        assert hasattr(req, 'json')
        assert req.status_code == 404