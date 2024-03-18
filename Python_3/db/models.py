from .database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql.schema import  ForeignKey
from sqlalchemy.orm import relationship

class DbUser(Base):
    __tablename__='artist'
    artist_id = Column(Integer, primary_key=True, index=True)
    artist_name = Column(String)
    password = Column(String)
    email = Column(String)
    artworks = str
    items = relationship('DbArtwork', back_populates='artist')

class DbArtwork(Base):
    __tablename__='artwork'
    artwork_id = Column(Integer, primary_key=True, index=True)
    artwork_name = Column(String)
    timestamp = Column(DateTime)
    artist_id = Column(Integer, ForeignKey('artist.artist_id'))
    artist = relationship('DbUser', back_populates='items')

