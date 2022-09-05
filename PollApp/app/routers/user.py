from tkinter.messagebox import NO
from .. import models, schemas, utils
from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import SessionLocal, engine, get_db


router = APIRouter(
    prefix="/users",
    tags=['users'] 

)

@router.get('/', response_model=List[schemas.ShowUser])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.get('/{id}', response_model=schemas.ShowUser)
def get_one_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    return user

@router.post('/', response_model=schemas.CreateUser)
def create_user(user : schemas.CreateUser, db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.put('/{id}', response_model= schemas.UpdateUser)
def update_user(id: int, updated_user: schemas.UpdateUser, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id == id)
    user = user_query.first()

    user_query.update(updated_user.dict(), synchronize_session= False)
    db.commit()
    return user_query.first()


@router.delete('/{id}', response_model=schemas.DeleteUser)
def delete_user(id: int, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id == id)
    user =user_query.first()

    user_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)