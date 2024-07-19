import pymysql
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_url = 'mysql+mysqlconnector://avnadmin:AVNS_g4ffSjirusDWXF9IJy1@mysql-30e7473a-afsheenzaahrah25-614f.i.aivencloud.com/demo'
#engine--establishes a connection to the database and handles the communication
engine=create_engine(database_url)
#declarative_base--establish link b/w Python class and db table
Base=declarative_base()
class Constants(Base):
    __tablename__ = 'credentials'
    id = Column(Integer, primary_key=True)
    database= Column(String(50), unique=True, nullable=False)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), unique=True, nullable=False)
    
Base.metadata.create_all(engine)
#session--manage db interactions and it offers methods to effectively manage CRUD operations.
Session = sessionmaker(bind=engine)
session = Session()
new_user1 = User(database='products', username='harini', password='rapid10')
new_user2 = User(database='city', username='sharuk', password='kwidaz')
session.add(new_user1)
session.add(new_user2)
session.commit()
all_users = session.query(User).all()
user = session.query(User).filter_by(username='sharuk').first()
session.close()
print(all_users)
print(user)