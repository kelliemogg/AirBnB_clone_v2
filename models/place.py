#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id' nullable=False),
                             primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id' nullable=False),
                             primary_key=True))

class Place(BaseModel, Base):
    """ A place to stay """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
