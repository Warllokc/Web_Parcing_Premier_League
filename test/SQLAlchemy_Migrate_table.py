from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from  sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://oisolqzxghhhjp:e3a898afdb19bea8c2b6864347f1da303f6fdfe443637715112252cffd87d9d6@'
                       'ec2-3-224-157-224.compute-1.amazonaws.com:5432/d8uo0fbra6958c', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Example(Base):
    __tablename__ = "Primier_League_players"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    country = Column(String(50))
    image_link = Column(String(150))
    position = Column(String(30))
    date_of_birth = Column(String(15))
    height = Column(String(10))
    player_link = Column(String(100))

Base.metadata.create_all(engine)



