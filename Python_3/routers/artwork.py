from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from routers.schemas import ArtworkBase, ArtworkDisplay, ArtistAuth
from db.database import get_db
from db import db_artwork
from auth.oauth2 import get_current_artist
from typing import List

router = APIRouter(
    prefix='/artwork',
    tags=['artwork']
)

@router.post('', response_model=ArtworkDisplay)
def create_artwork(request: ArtworkBase, db: Session = Depends(get_db), current_artist: ArtistAuth = Depends(get_current_artist)):
    return db_artwork.create_artwork(db, request)

@router.get('/all', response_model=List[ArtworkDisplay])
def artwork(db: Session = Depends(get_db)):
    return db_artwork.get_all(db)

@router.get('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db), current_user: ArtistAuth = Depends(get_current_artist)):
    return db_artwork.delete(db, id, current_user.artist_id)


    