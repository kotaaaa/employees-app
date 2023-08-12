from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from api.models.employee import Base
from api.models.employee import Employee

DB_URL = "mysql+pymysql://root@db:3306/employees?charset=utf8"
engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

import json

with open("data.json", "r") as file:
    data = json.load(file)
employees_data = data["employees"]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def reset_database():
    db = next(get_db())
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    for emp in employees_data:
        db_employee = Employee(**emp)
        db.add(db_employee)
    db.commit()

    return {"message": "Database initialized!"}


if __name__ == "__main__":
    reset_database()
