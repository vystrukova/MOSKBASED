import pytest
import requests


def test_get():
    response = requests.get(url='https://api.sampleapis.com/avatar/characters/')
    print(f'Status code: {response.status_code}')
    print(f'Headers: {response.headers}')
    print(f'Body: {response.json()}'.encode('utf-8'))


def test_get_second():
    params = {
        'name': 'Aang'
    }
    response = requests.get(url='https://api.sampleapis.com/avatar/characters/', params=params)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body[0]['name'] == params['name']


def test_post():
    json = {
        "name": "Floppa",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Gregory_and_watermelon.jpg/1920px-Gregory_and_watermelon.jpg",
        "bio": {},
        "physicalDescription": {},
        "personalInformation": {},
        "politicalInformation": {},
        "chronologicalInformation": {}
    }

    response = requests.post(url='https://api.sampleapis.com/avatar/characters/', json=json)
    print(response.status_code)
    print(response.json())


@pytest.mark.skip
def test_put():
    json = {
        "name": "Based Floppa",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Gregory_and_watermelon.jpg/1920px-Gregory_and_watermelon.jpg",
        "bio": {},
        "physicalDescription": {},
        "personalInformation": {},
        "politicalInformation": {},
        "chronologicalInformation": {}
    }
    response = requests.put(url='https://api.sampleapis.com/avatar/characters/15', json=json)
    assert response.status_code == 200
    response_body = response.json()
    #assert response_body['name'] == data['name']

