#the client here is a django fixture
#so it doesn't need import

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
