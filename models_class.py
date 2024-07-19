from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from constants import ConnectDatabase
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.orm import sessionmaker

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    email:Mapped[str] = mapped_column(String(30))
    gender:Mapped[str] = mapped_column(String(30))
    ip_address:Mapped[str] = mapped_column(String(30))

# if __name__ == "__main__":
#     db = ConnectDatabase()
#     engine = db.make_session
#     #Base.metadata.create_all(engine)
#     print("table user created successfully")
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     new = User(first_name='John',last_name='Doe',email='john.doe@example.com',gender='male',ip_address= 192)
#     session.add(new)
#     users = session.query(User).all()

#     print(users)


