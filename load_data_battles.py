import pandas as pd
from got.models import Battles
from got import db

df_characters = pd.read_csv('data/batlles.csv')


for i, row in df_characters.iterrows():
    char = Battles()
    char.name  = row['Name']
    char.year = row['Year']
    char.battle_number = row['Battle Number']
    char.attacker_king = row['Attacker King']
    char.defender_king = row['Defender King']
    char.attacker_1 = row['Attacker 1']
    char.attacker_2 = row['Attacker 2']
    char.attacker_3 = row['Attacker 3']
    char.attacker_4 = row['Attacker 4']
    char.defender_1 =  row['Defender 1']
    char.defender_2 =  row['Defender 2']
    char.defender_3 =  row['Defender 3']
    char.defender_4 =  row['Defender 4']
    char.attacker_outcome = row['Attacker Outcome']
    char.battle_type = row['Battle Type']
    char.major_death = row['Major Death']
    char.major_capture = row['Major Capture']
    char.attacker_size = row['Attacker Size']
    char.defender_size = row['Defender Size']
    char.attacker_commander = row['Attacker Commander']
    char.defender_commander = row['Defender Commander']
    char.summer = row['Summer']
    char.location = row['Location']
    char.region = row['Region']
    char.note = row['Note']

    db.session.add(char)
    db.session.query(Battles).all()

db.session.commit()