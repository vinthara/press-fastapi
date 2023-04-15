import pytest
from .. import schemas


def test_root(client):
    res = client.get("/")
    assert res.status_code == 222


def test_create_user(client):
    client
    res = client.post(
        "/user",
        json={
            "first_name": "hello",
            "last_name": "123",
            "email": "hello123@gmail.com",
            "password": "password123",
        },
    )

    new_user = schemas.UserCreate(**res.json())
    assert new_user.email == "hello123@gmail.com"
    assert res.status_code == 200
