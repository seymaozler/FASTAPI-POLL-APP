from asyncore import poll
from tkinter.messagebox import NO
from .. import models, schemas, oauth2
from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import SessionLocal, engine, get_db


router = APIRouter(
    prefix="/polls",
    tags=['polls'] 

)

@router.get('/', response_model= List[schemas.ShowPoll])
def get_polls(db: Session = Depends(get_db)):
    polls = db.query(models.Poll).all()
    return polls

@router.get('/{id}', response_model=schemas.ShowPoll)
def get_one_poll(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    poll = db.query(models.Poll).filter(models.Poll.id == id).first()

    return poll

@router.post('/', response_model=schemas.CreatePoll)
def create_poll(poll : schemas.CreatePoll,  db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_poll = models.Poll(**poll.dict())
    db.add(new_poll)
    db.commit()
    db.refresh(new_poll)

    return new_poll

@router.put('/{id}', response_model=schemas.UpdatePoll)
def update_poll(id: int, updated_poll: schemas.UpdatePoll, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    poll_query = db.query(models.Poll).filter(models.Poll.id == id)
    poll = poll_query.first()

    poll_query.update(updated_poll.dict(), synchronize_session= False)
    db.commit()
    return poll_query.first()

@router.delete('/{id}', response_model=schemas.DeletePoll)
def delete_poll(id: int, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    poll_query = db.query(models.Poll).filter(models.Poll.id == id)

    poll = poll_query.first()

    poll_query.delete(synchronize_session= False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)