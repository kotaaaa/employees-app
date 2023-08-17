from sqlalchemy import Column, Integer, String

from api.db import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(1024))
    last_name = Column(String(1024))
    job_title = Column(String(1024))
    salary = Column(Integer)
