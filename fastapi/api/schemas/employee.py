from typing import Optional

from pydantic import BaseModel, Field


class EmployeeBase(BaseModel):
    first_name: Optional[str] = Field(None, example="Mike")
    last_name: Optional[str] = Field(None, example="Trout")
    salary: Optional[int] = Field(None, example=100000)


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeCreateResponse(EmployeeCreate):
    id: int

    class Config:
        orm_mode = True


class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True


class EmployeeDeleteResponse(BaseModel):
    status: bool
