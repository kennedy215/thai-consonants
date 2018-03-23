# -*- coding: utf-8 -*-

#This setup is great for a database that intergrates the other database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import sys

from database_list import Base,lowConsonants

# detecting Thai language format
# from language_detect import detect



engine = create_engine('sqlite:///thaiconsonants.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session =DBSession()

# Information to be intergrated

#Chicken
chicken = lowConsonants(name="Chicken",thai_consonant="ก",thai_spelling="x",sound="k/k")


session.add(chicken)
session.commit()

# toneMid = Tones(name="Mid")





# class Consonants(Base):
#     __tablename__ = 'consonants'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#     thai_consonant = Column(String(1))
#     thai_spelling = Column(String(10))
#     sound = Column(String(10))
#     tone = Column(String(5))
#
# class Tones(Base)
#     __tablename__ = 'tones'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#     consonant_tone = Column(Integer, ForeignKey('consonants.id'))
#     consonants = relationship(Consonants)
