from sqlalchemy.ext.asyncio import AsyncSession

import api.models.employee as employee_model
import api.schemas.employee as employee_schema
from typing import List, Tuple

from sqlalchemy import select
from sqlalchemy.engine import Result


async def create_employee(
    db: AsyncSession, employee_create: employee_schema.EmployeeCreate
) -> employee_model.Employee:
    employee = employee_model.Employee(**employee_create.dict())
    db.add(employee)
    await db.commit()
    await db.refresh(employee)
    return employee


async def get_employees(db: AsyncSession) -> List[Tuple[int, str, str, int]]:
    result: Result = await db.execute(
        select(
            employee_model.Employee.id,
            employee_model.Employee.first_name,
            employee_model.Employee.last_name,
            employee_model.Employee.salary,
        )
    )
    return result.all()


from typing import List, Tuple, Optional


async def get_employee(
    db: AsyncSession, employee_id: int
) -> Optional[employee_model.Employee]:
    result: Result = await db.execute(
        select(employee_model.Employee).filter(
            employee_model.Employee.id == employee_id
        )
    )
    employee: Optional[Tuple[employee_model.Employee]] = result.first()
    return (
        employee[0] if employee is not None else None
    )  # Retrieve the first element since it is returned in tuple even if there is only one element.


async def update_employee(
    db: AsyncSession,
    employee_create: employee_schema.EmployeeCreate,
    original: employee_model.Employee,
) -> employee_model.Employee:
    original.first_name = employee_create.first_name
    original.last_name = employee_create.last_name
    original.salary = employee_create.salary
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_employee(db: AsyncSession, original: employee_model.Employee) -> None:
    await db.delete(original)
    await db.commit()
    return {"status": True}  # TODO ERROR handling
