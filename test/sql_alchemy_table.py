from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from  sqlalchemy.ext.declarative import declarative_base
from tqdm import tqdm
engine = create_engine('postgresql://oisolqzxghhhjp:e3a898afdb19bea8c2b6864347f1da303f6fdfe443637715112252cffd87d9d6@'
                       'ec2-3-224-157-224.compute-1.amazonaws.com:5432/d8uo0fbra6958c', echo=True)

Session = sessionmaker(bind=engine)
session = Session()
id = 1

Base = declarative_base()

class Player_Table(Base):
    __tablename__ = "Primier_League_players"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    country = Column(String(50))
    image_link = Column(String(150), unique=True)
    position = Column(String(30))
    date_of_birth = Column(String(15))
    height = Column(String(10))
    player_link = Column(String(100), unique=True)

Base.metadata.create_all(engine)

def add_player_data(name, country, image, position, date, height,link):
    global id
    players_table = session.query(Player_Table).all()
    pbar = tqdm(total=len(players_table))
    player_data = Player_Table()

    for player in players_table:
        key = session.query(Player_Table).filter_by(id=player.id).first()
        if key in players_table:
                id+=1
    existed_player = session.query(Player_Table).filter_by(name=name).first()

    if existed_player in players_table:
        print()
        return "Player already added to DB"

    else:

        player_data.id = id
        player_data.name = name
        player_data.country = country
        player_data.image_link = image
        player_data.position = position
        player_data.date_of_birth = date
        player_data.height = height
        player_data.player_link = link
        session.add(player_data)
        pbar.update(1)
        id+=1
        session.commit()

def delete_player_data(player_name):
    players_data = session.query(Player_Table).all()
    pbar = tqdm(total=len(players_data))
    for player in players_data:
        premier = session.query(Player_Table).filter_by(name=player_name).first()
        premier.status = True
        pbar.update(1)
    session.delete(premier)
    session.commit()

def update_player_name(old_player_name, new_name):
    players_data = session.query(Player_Table).all()
    pbar = tqdm(total=len(players_data))
    for player in players_data:
        if player.name == old_player_name:
           player.name = Player_Table(name=new_name).name
    pbar.update(1)
    session.commit()


############# parsing JSON file
add_player_data("David Seaman","England","resources.premierleague.com/premierleague/photos/players/250x250/p9.png",
                "Goalkeeper", "19/09/1963", "193cm", "https://www.premierleague.com/players/1")
delete_player_data("David Seaman")
update_player_name("David Seaman", "alex")