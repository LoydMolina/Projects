from routers.schemas import ArtworkBase
from sqlalchemy.orm.session import Session
from db.models import DbArtwork
import datetime
from fastapi import HTTPException, status

def create_artwork(db: Session, request: ArtworkBase):
    new_artwork = DbArtwork(
        artwork_name = request.artwork_name,
        timestamp = datetime.datetime.now(),
        artist_id = request.artist_id
    )
    db.add(new_artwork)
    db.commit()
    db.refresh(new_artwork)
    return new_artwork

def get_all(db: Session):
    return db.query(DbArtwork).all()

def delete(db: Session, id: int, artist_id: int):
    artwork = db.query(DbArtwork).filter(DbArtwork.artwork_id == id).first()
    if not artwork:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f'Post with id {id} not found')
    if artwork.artist_id != artist_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail = 'Only creator can delete artwork.')
    db.delete(artwork)
    db.commit()
    return f'Post with id {id} has been deleted.'