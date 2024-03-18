from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    artist_name: str
    email: str
    password: str

class UserDisplay(BaseModel):
    artist_name: str
    email: str
    artist_id: int

    class Config():
        orm_mode = True


class ArtworkBase(BaseModel):
    artwork_name: str
    artist_id: int

class Artist(BaseModel):
    artist_name: str
    class Config():
        orm_mode = True

    
class ArtworkDisplay(BaseModel):
    artwork_id: int
    artwork_name: str
    timestamp: datetime
    artist: Artist
    class Config():
        orm_mode = True

class ArtistAuth(BaseModel):
    artist_id: int
    artist_name: str
    email: str