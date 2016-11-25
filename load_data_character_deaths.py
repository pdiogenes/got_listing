import pandas as pd
from got.models import CharacterDeaths
from got import db

df_characters = pd.read_csv('data/character-deaths.csv')


for i, row in df_characters.iterrows():
    char = CharacterDeaths()
    char.name  = row['Name']
    char.death_year = row['Death Year']
    char.book_of_death = row['Book of Death']
    char.death_chapter = row['Death Chapter']
    char.book_intro_chapter = row['Book Intro Chapter']
    char.gender = row['Gender']
    char.nobility = row['Nobility']
    char.got = row['GoT']
    char.cok = row['CoK']
    char.sos =  row['SoS']
    char.ffc = row['FfC']
    char.dwd = row['DwD']

    db.session.add(char)
    db.session.query(CharacterDeaths).all()

db.session.commit()