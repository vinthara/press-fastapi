from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int | None
    first_name: str
    last_name: str
    nickname: str | None
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    nickname: str | None
    email: EmailStr

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: str | None
    # created_at: datetime
