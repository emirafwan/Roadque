from sqlalchemy.orm import Session
from . import models, schemas

def get_images(db: Session):
    return db.query(models.Images).all()

def get_image_by_id(db: Session, id:int):
    return db.query(models.Images).filter(models.Images.id==id).first()

def get_locations(db: Session):
    return db.query(models.Location).all()

def get_location_by_id(db: Session, id:int):
    return db.query(models.Location).filter(models.Location.id==id).first()


def post_location(db: Session, loc = schemas.LocationCreate, id=int):
    reg = loc.region
    lat = loc.latitude 
    lon = loc.longitude 
    db_addloc = models.Location(id=id, region=reg, latitude=lat ,longitude=lon)
    db.add(db_addloc)
    db.commit()
    db.refresh(db_addloc)
    return db_addloc

def post_dataset(db: Session, image:schemas.ImagesCreate, location:schemas.LocationCreate):
    reg = location.region
    lat = location.latitude
    lon = location.longitude
    url= image.image_url
    loc_id = location.id

    db_loc = models.Location(id = loc_id, region=reg, latitude=lat ,longitude=lon)
    db_img = models.Images(image_url=url, location_id=loc_id)

    db.add(db_loc)
    db.commit()
    db.refresh(db_loc)
    db.add(db_img)
    db.commit()
    db.refresh(db_img)
    return db_img




   