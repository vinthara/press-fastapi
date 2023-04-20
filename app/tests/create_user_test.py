import pytest
from .. import schemas


def test_root(client):
    res = client.get("/")
    assert res.status_code == 200


def test_create_user(client):
    res = client.post(
        "/user",
        json={
            "first_name": "hello",
            "last_name": "123",
            "email": "hello123@gmail.com",
            "password": "password123",
        },
    )

    new_user = schemas.User(**res.json())
    assert new_user.email == "hello123@gmail.com"
    assert res.status_code == 200


def test_get_all_users(authorized_client):
    res = authorized_client.get("/users")
    all_users = schemas.User(**res.json()[0])
    assert all_users.email == "aravinthbalakrishnan@gmail.com"
