from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from .database import Base
import datetime
from datetime import datetime, time, timedelta
from sqlalchemy.types import TIMESTAMP



class Images(Base):
    __tablename__='images'
    id = Column(Integer, primary_key=True)
    image_url = Column(String(250), nullable=False)
    location_id =  Column(Integer, ForeignKey('location.id'))
    location = relationship("Location", back_populates="image")

class Location(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True)
    region = Column(String(250), nullable=False)
    latitude = Column(Float(25), nullable=False)
    longitude = Column(Float(25), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
    image = relationship("Images", back_populates="location")
    



