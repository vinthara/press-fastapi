from pydantic import BaseModel, EmailStr


class Employee(BaseModel):
    id: int | None
    first_name: str
    last_name: str
    nickname: str | None
    email: EmailStr
    is_super_admin: bool

    class Config:
        orm_mode = True


class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    nickname: str | None
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class EmployeeLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: str | None
    # created_at: datetime
