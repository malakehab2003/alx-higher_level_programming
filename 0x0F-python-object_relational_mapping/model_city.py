#!/usr/bin/python3
""" make state class"""
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class City(Base):
    """ the city class to table of db"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True,
                unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
