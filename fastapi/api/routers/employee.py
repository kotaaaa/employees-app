from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import api.cruds.employee as employee_crud
from api.db import get_db
import api.schemas.employee as employee_schema
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(prefix="/api")


@router.get("/employees", response_model=List[employee_schema.Employee])
async def list_employees(db: AsyncSession = Depends(get_db)):
    """_summary_

    Args:
        db (AsyncSession, optional): _description_. Defaults to Depends(get_db).

    Returns:
        List[employee_schema.Employee]: List of Employee Model
    """
    return await employee_crud.get_employees(db)


@router.post("/employees", response_model=employee_schema.EmployeeCreateResponse)
async def create_employee(
    employee_body: employee_schema.EmployeeCreate, db: AsyncSession = Depends(get_db)
):
    """Get all employee's name and salary.

    Args:
        employee_body (employee_schema.EmployeeCreate): _description_
        db (AsyncSession, optional): _description_. Defaults to Depends(get_db).

    Returns:
        EmployeeCreateResponse: Created Employee object.
    """
    return await employee_crud.create_employee(db, employee_body)


@router.put(
    "/employees/{employee_id}", response_model=employee_schema.EmployeeCreateResponse
)
async def update_employee(
    employee_id: int,
    employee_body: employee_schema.EmployeeCreate,
    db: AsyncSession = Depends(get_db),
):
    """Update employee's name or salary.

    Args:
        employee_id (int): id for each employee
        employee_body (employee_schema.EmployeeCreate): Employee model from frontend
        db (AsyncSession, optional): db session. Defaults to Depends(get_db).

    Raises:
        HTTPException:

    Returns:
        EmployeeCreateResponse: Created Employee object.
    """
    employee = await employee_crud.get_employee(db, employee_id=employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return await employee_crud.update_employee(db, employee_body, original=employee)


@router.delete(
    "/employees/{employee_id}", response_model=employee_schema.EmployeeDeleteResponse
)
async def delete_employee(employee_id: int, db: AsyncSession = Depends(get_db)):
    """Delete specifix employee_id's information

    Args:
        employee_id (int): id for each employee
        db (AsyncSession, optional): db session. Defaults to Depends(get_db).

    Raises:
        HTTPException:

    Returns:
        json: {status: bool}
    """
    employee = await employee_crud.get_employee(db, employee_id=employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return await employee_crud.delete_employee(db, original=employee)
