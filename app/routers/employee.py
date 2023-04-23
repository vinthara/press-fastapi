from pydantic import typing
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException, status
from ..database import engine, get_db

from ..oauth2 import get_current_employee_id


from .. import schemas, utils, models
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
router = APIRouter(tags=["Employee"])


@router.post("/employee", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    new_employee = models.Employee(**employee.dict())

    email_already_in_database = (
        db.query(models.Employee)
        .filter(models.Employee.email == new_employee.email)
        .first()
    )
    if email_already_in_database:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Email is already in use"
        )

    new_employee.password = pwd_context.hash(new_employee.password)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee


@router.get("/employees", response_model=list[schemas.Employee])
def get_all_employees(
    db: Session = Depends(get_db), employee=Depends(get_current_employee_id)
):
    employees = db.query(models.Employee).all()

    return employees
