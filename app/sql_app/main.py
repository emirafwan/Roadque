from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello Roadque Teams!"}

@app.get("/images/", response_model=List[schemas.Images])
async def read_images(db: Session = Depends(get_db)):
    images = crud.get_images(db)
    return images

@app.get("/images/{image_id}", response_model=schemas.Images)
async def read_image(image_id:int, db: Session = Depends(get_db)):
    db_image = crud.get_image_by_id(db, id=image_id)
    if db_image is None:
        raise HTTPException(status_code=404, detail = "image not found")
    return db_image

@app.get("/locations/", response_model=List[schemas.Locations])
async def read_locaions(db: Session = Depends(get_db)):
    locations = crud.get_locations(db)
    return locations

@app.get("/locations/{location_id}", response_model=schemas.Locations)
async def read_image(location_id:int, db: Session = Depends(get_db)):
    db_location = crud.get_location_by_id(db, id=location_id)
    if db_location is None:
        raise HTTPException(status_code=404, detail = "locaiton not found")
    return db_location

@app.post("/dataset", response_model= schemas.ImgnLoc)
async def create_dataset(image:schemas.ImagesCreate, location:schemas.LocationCreate, db: Session = Depends(get_db)):
    db_conf = crud.get_location_by_id(db, id=location.id)
    if db_conf:
        raise HTTPException(status_code=400, detail="data already registered")
    return crud.post_dataset(db=db, image=image, location=location)
