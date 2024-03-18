from db.models import DbUser
from routers.schemas import UserBase
from sqlalchemy.orm.session import Session
from db.hashing import Hash
from fastapi import HTTPException, status

def create_artist(db: Session, request: UserBase):
    new_artist = DbUser(
        artist_name = request.artist_name,
        password = Hash.bcrypt(request.password),
        email = request.email
    )
    db.add(new_artist)
    db.commit()
    db.refresh(new_artist)
    return new_artist

def update_artist(db: Session, id: int, request: UserBase):
    artist = db.query(DbUser).filter(DbUser.artist_id == id)
    artist.update ({
        DbUser.artist_name: request.artist_name,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return 'Update complete.'

def get_artist_by_artistname(db: Session, artist_name: str):
    artist = db.query(DbUser).filter(DbUser.artist_name == artist_name).first()
    if not artist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        details = f'Artist with artist name {artist_name} not found')
    return artist

def delete_artist(db: Session, id: int):
    artist = db.query(DbUser).filter(DbUser.artist_id == id).first()
    db.delete(artist)
    db.commit()
    return 'Artist Deleted.'