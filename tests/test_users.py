import pytest
from django.test import Client
from apps.users.models import User

@pytest.mark.django_db
def test_register_success():
    client = Client()
    response = client.post(
        "/api/users/register",
        data={"username": "testuser", "password": "123456"},
        content_type="application/json"
    )
    assert response.status_code == 200
    assert "token" in response.json()
@pytest.mark.django_db
def test_register_duplicate_username():
    User.objects.create_user(username="testuser", password="123456")
    client = Client()
    response = client.post(
        "/api/users/register",
        data={"username": "testuser", "password": "123456"},
        content_type="application/json"
    )
    assert response.status_code == 400
@pytest.mark.django_db
def test_login_success():
    user = User.objects.create_user(username="testuser", password="123456")
    client = Client()

    response = client.post(
        "/api/users/login",
        data={"username": "testuser", "password": "123456"},
        content_type="application/json"
    )
    assert response.status_code == 200
    assert "token" in response.json()
@pytest.mark.django_db
def test_login_invalid_credentials():
    client = Client()

    response = client.post(
        "/api/users/login",
        data={"username": "nope", "password": "wrong"},
        content_type="application/json"
    )
    assert response.status_code == 401