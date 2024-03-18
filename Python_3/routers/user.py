from fastapi import APIRouter, Depends
from routers.schemas import UserDisplay, UserBase
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_user

router = APIRouter(
    prefix='/artist',
    tags=['artist']
)

@router.post('', response_model=UserDisplay)
def create_artist(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_artist(db, request)

@router.post('/update/{id}')
def update_artist(id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_artist(db, id, request)

@router.get('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    return db_user.delete_artist(db, id)