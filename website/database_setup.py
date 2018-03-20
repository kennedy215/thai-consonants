import os
import sys
# import table properties from SQL Alchemy
from sqlalchemy import Column, ForeignKey, String, Integer
# import declarative_base from the SQL Alchemy extension declarative
from sqlalchemy.ext.declarative import declarative_base
# import relationshi from sqlalchemy.orm
from sqlalchemy.orm import relationship
# ability to create engine

from sqlalchemy import create_engine

Base = declarative_base()


class Tenant(Base):
    __tablename__ = 'restaurant'
    # indicating if name is not filled out we cannot create another
    # restaurant row in the database
    name = Column(String(20), nullable=False)
    id = Column(Integer, primary_key=True)


class Room(Base):
    __tablename__ = 'menu_item'
    # make sure no one can create a menu item without a name.
    name = Column(String(20), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    tenant_id = Column(Integer, ForeignKey('tenant.id'))
    tenant = relationship(Tenant)


# This always goes to the end
engine = create_engine('sqlite:///website.db')
Base.metadata.create_all(engine)


print "It worked!!!!!"
