''' from fastapi import APIRouter
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from .database import SessionLocal, engine


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/image/", response_model=schemas.Images)
async def read_image(skip:str= 0, limit:str= 100, db:Session = Depends(get_db())):
    db_image = crud.get_image(db, image_id=image_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_image


@router.get("/location")
async def read_location():
    return [{"location_id":"1",
            "latitude":"-6.207270",
            "longitude":"106.960899",
            "created_at":"",
            "updated_at":""}]

@router.get("/validation")
async def read_validation():
    return [{"location_id":"1",
            "verification_id":"1",
            "image_id":"1"}]
            '''
