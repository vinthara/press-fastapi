import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from ..main import app
from ..config import settings
from ..database import Base, get_db
from .. import models
from app.oauth2 import create_access_token


SQLALCHEMY_DATABASE_TEST_URL = settings.sqlalchemy_database_test_url

engine = create_engine(
    SQLALCHEMY_DATABASE_TEST_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture
def test_user(client):
    user_data = {
        "first_name": "Aravinth",
        "last_name": "Balakrishnan",
        "email": "aravinthbalakrishnan@gmail.com",
        "password": "password123",
    }
    res = client.post("/user", json=user_data)

    assert res.status_code == 200

    new_user = res.json()
    new_user["password"] = user_data["password"]
    return new_user


@pytest.fixture
def token(test_user):
    return create_access_token({"user_id": test_user["id"]})


@pytest.fixture
def authorized_client(client, token):
    client.headers = {**client.headers, "Authorization": f"Bearer {token}"}
    return client


# def test_root(client):
#     res = client.get("/")
