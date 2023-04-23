import pytest
from .. import schemas


def test_root(client):
    res = client.get("/")
    assert res.status_code == 200


def test_create_employee(client):
    res = client.post(
        "/employee",
        json={
            "first_name": "hello",
            "last_name": "123",
            "email": "hello123@gmail.com",
            "password": "password123",
        },
    )

    new_employee = schemas.Employee(**res.json())
    assert new_employee.email == "hello123@gmail.com"
    assert res.status_code == 200


def test_get_all_employees(authorized_client):
    res = authorized_client.get("/employees")
    all_employees = schemas.Employee(**res.json()[0])
    assert all_employees.email == "aravinthbalakrishnan@gmail.com"
