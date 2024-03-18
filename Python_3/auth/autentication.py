from fastapi import APIRouter, HTTPException, status,Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from db.database import get_db
from sqlalchemy.orm.session import Session
from db.models import DbUser
from db.hashing import Hash
from auth.oauth2 import create_access_token


router = APIRouter(
    tags=['authentication']
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    artist = db.query(DbUser).filter(DbUser.artist_name == request.username).first()
    if not artist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail = 'Invalid Credentials')
    if not Hash.verify(artist.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail='Incorrect password')
    
    access_token = create_access_token(data = {'artist_name': artist.artist_name})

    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'artist_id': artist.artist_id,
        'artist_name': artist.artist_name
    }