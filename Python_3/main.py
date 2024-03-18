from fastapi import FastAPI
from db.database import engine
from db import models
from routers import user, artwork
from auth import autentication

app = FastAPI()

app.include_router(user.router)
app.include_router(artwork.router)
app.include_router(autentication.router)

@app.get('/')
def root():
    return {'message': f'sample-api'}

models.Base.metadata.create_all(engine)