from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from clientlist_database import Base, Tenant, Room

engine = create_engine('sqlite:///tenant_database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession

#client
# tenant1 = Tenant(f_name="Jim", l_name="Bean", email="jimbeandrinks@hotmail.com")
#
# session.add(tenant1)
# session.commit()
tenant1 = Tenant(f_name="Byron", l_name="Marrow", email="B@hotmail.com")

session.add(tenant1)
session.commit()

#room
room1 = Room(room="100", price="$150.00", repairs="none", tenant = tenant1)

session.add(room1)
session.commit()

print "It's all added!!!"
