from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Date,
    Time,
    UniqueConstraint,
    CheckConstraint,
)
from sqlalchemy import sql
from sqlalchemy.orm import relationship

from .database import Base


class Employee(Base):
    __tablename__ = "EMPLOYEE"

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    nickname = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_super_admin = Column(Boolean, nullable=False, default=False)


class Press(Base):
    __tablename__ = "PRESS"

    id = Column(String, primary_key=True, nullable=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    zip_code = Column(Integer, nullable=False)


class EmployeeRole(Base):
    __tablename__ = "EMPLOYEE_ROLE"

    employee_id = Column(
        Integer, ForeignKey("EMPLOYEE.id"), primary_key=True, nullable=False
    )
    press_id = Column(String, ForeignKey("PRESS.id"), primary_key=True, nullable=False)
    is_employee = Column(Boolean, nullable=False, default=False)
    is_admin = Column(Boolean, nullable=False, default=False)


class EmployeeWeekCalendar(Base):
    __tablename__ = "EMPLOYEE_WEEK_CALENDAR"
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("EMPLOYEE.id"), nullable=False)
    press_id = Column(String, ForeignKey("PRESS.id"), nullable=False)
    week_day = Column(Integer, nullable=False)
    shift_number = Column(Integer, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    UniqueConstraint(employee_id, press_id, week_day, shift_number)
    CheckConstraint("start_time < end_time")
