import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()

# 1. Write and classify consonants in the database
# 2. Get the list that was selected and populate in the template

class Tenant(Base):
    __tablename__ = 'tenant'

    id = Column(Integer, primary_key=True)
    f_name = Column(String(250), nullable=False)
    l_name = Column(String(250))
    email = Column(String(30))


class Room(Base):
    __tablename__ = 'room'

    id = Column(Integer, primary_key=True)
    room = Column(String(3))
    price = Column(String(7))
    repairs = Column(String(500))
    tenant_id = Column(Integer, ForeignKey('tenant.id'))
    tenant = relationship(Tenant)


engine = create_engine('sqlite:///tenant_database.db')

Base.metadata.create_all(engine)
