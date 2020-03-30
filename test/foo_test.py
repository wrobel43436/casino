def test_one(client):
    response = client.get('/')
    assert response.status_code == 200


def test_valid_user(client):
    json = {"email": "tomek@gmail.com",
            "firstName": "Tomek",
            "lastName": "Wrobel",
            "isAdmin": False,
            "isActive": True,
            "lastLogin": "01.01.20",
            "password": "password"}
    response = client.post('/user', json = json)
    assert response.status_code == 200
    assert response.json['email'] == json['email']
    assert response.json['firstName'] == 'lukasz'

def test_not_valid_user(client):
    json = {"email": "tomek@hotmail.com",
            "firstName": "Tomek",
            "lastName": "Wrobel",
            "isAdmin": False,
            "isActive": True,
            "lastLogin": "01.01.20",
            "password": "password"}
    response = client.post('/user', json = json)
    assert response.status_code == 400
    assert response.json['wrong'] == ['email not supported']
