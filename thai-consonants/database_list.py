# -*- coding: utf-8 -*-
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# 1. Write and classify consonants in the database
# 2. Get the list that was selected and populate in the template

class lowConsonants(Base):
    __tablename__ = 'low_consonants'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    thai_consonant = Column(String(1))
    thai_spelling = Column(String(10))
    sound = Column(String(10))
    tone = Column(String(5))

engine = create_engine('sqlite:///thaiconsonants.db')

Base.metadata.create_all(engine)
