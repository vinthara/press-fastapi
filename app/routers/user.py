from pydantic import typing
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException, status
from ..database import engine, get_db

from ..oauth2 import get_current_user_id


from .. import schemas, utils, models
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
router = APIRouter(tags=["User"])


@router.post("/user", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(**user.dict())

    email_already_in_database = (
        db.query(models.User).filter(models.User.email == new_user.email).first()
    )
    if email_already_in_database:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Email is already in use"
        )

    new_user.password = pwd_context.hash(new_user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/users", response_model=list[schemas.User])
def get_all_users(db: Session = Depends(get_db), user=Depends(get_current_user_id)):
    users = db.query(models.User).all()

    return users
