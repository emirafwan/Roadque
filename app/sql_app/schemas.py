from typing import List, Optional
from pydantic import BaseModel


class ImageBase(BaseModel):
    image_url:str
    
class Images(ImageBase):
    id:int
    location_id:int

    class Config:
        orm_mode = True

class ImagesCreate(ImageBase):
    pass
class LocationBase(BaseModel):
    id:int
    region:str
    latitude :float
    longitude:float

    class Config:
        orm_mode = True

class Locations(LocationBase):
    pass

class LocationCreate(LocationBase):
    pass

class ImgnLoc(BaseModel):
    image:ImagesCreate
    location:LocationCreate
