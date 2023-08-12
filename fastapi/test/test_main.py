import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from api.db import get_db, Base
from api.main import app
import starlette.status


ASYNC_DB_URL = "sqlite+aiosqlite:///:memory:"


@pytest.fixture
async def async_client() -> AsyncClient:
    # Create engine and session for Async
    async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
    async_session = sessionmaker(
        autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
    )

    # Initialize on-memory SQLite tables for testing (reset per function)
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    # Use DI to change FastAPI's DB destination to test DB
    async def get_test_db():
        async with async_session() as session:
            yield session

    app.dependency_overrides[get_db] = get_test_db

    # Return asynchronous HTTP client for testing
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


import starlette.status


@pytest.mark.asyncio
async def test_create_and_read(async_client):
    # post request test
    response = await async_client.post(
        "/api/employees",
        json={"first_name": "Aaron", "last_name": "Judge", "salary": 1000000},
    )
    assert response.status_code == starlette.status.HTTP_200_OK
    response_obj = response.json()
    assert response_obj["first_name"] == "Aaron"

    # get request test
    response = await async_client.get("/api/employees")
    assert response.status_code == starlette.status.HTTP_200_OK
    response_obj = response.json()
    assert len(response_obj) == 1
    assert response_obj[0]["first_name"] == "Aaron"
    assert response_obj[0]["last_name"] == "Judge"
    assert response_obj[0]["salary"] == 1000000


@pytest.mark.asyncio
async def test_create_and_edit(async_client):
    # post request test
    response = await async_client.post(
        "/api/employees",
        json={"first_name": "Mike", "last_name": "Trout", "salary": 1000000},
    )
    assert response.status_code == starlette.status.HTTP_200_OK
    response_obj = response.json()
    assert response_obj["first_name"] == "Mike"
    assert response_obj["last_name"] == "Trout"
    assert response_obj["salary"] == 1000000

    # put request test
    response = await async_client.put(
        "/api/employees/1",
        json={"first_name": "Mike", "last_name": "Trout", "salary": 2000000},
    )
    assert response.status_code == starlette.status.HTTP_200_OK
    response_obj = response.json()
    assert response_obj["salary"] == 2000000


@pytest.mark.asyncio
async def test_create_and_delete(async_client):
    # post request test
    response = await async_client.post(
        "/api/employees",
        json={"first_name": "Shohei", "last_name": "Otani", "salary": 1000000},
    )
    assert response.status_code == starlette.status.HTTP_200_OK
    response_obj = response.json()
    assert response_obj["first_name"] == "Shohei"

    # delete request test
    response = await async_client.delete("/api/employees/1")
    assert response.status_code == starlette.status.HTTP_200_OK
    response_obj = response.json()
    assert response_obj == {"status": True}

    # get request test
    response = await async_client.get("/api/employees")
    assert response.status_code == starlette.status.HTTP_200_OK
    response_obj = response.json()
    assert len(response_obj) == 0
