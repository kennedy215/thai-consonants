import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# 1. Write and classify consonants in the database
# 2. Get the list that was selected and populate in the template

class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    f_name = Column(String(250), nullable=False)
    l_name = Column(String(250))
    email = Column(String(30))


class Room(Base):
    __tablename__ = 'room'

    id = Column(Integer, primary_key=True)
    room = Column(String(3))
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship(Client)


engine = create_engine('sqlite:///clientlist_database.db')

Base.metadata.create_all(engine)
