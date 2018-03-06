#This setup is great for a database that intergrates the other database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import sys

from clientlist_database import Client,Base,Room


engine = create_engine('sqlite:///clientlist_database.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session =DBSession()

# Information to be intergrated

#Chicken
client = Client(f_name="Chicken",l_name="Choco",email="chickenchoco@gmail.com")
session.add(client)

session.commit()

room = Room(room="100")
session.add(room)

session.commit()
