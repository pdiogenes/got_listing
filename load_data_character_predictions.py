import pandas as pd
from got.models import CharacterPredictions
from got import db

df_characters = pd.read_csv('data/character-predictions.csv')


for i, row in df_characters.iterrows():
    char = CharacterPredictions()
    char.S_No =row['S_No']
    char.actual =row['actual'] 
    char.pred =row['pred'] 
    char.alive =row['alive'] 
    char.plod =row['plod'] 
    char.name =row['name'] 
    char.title =row['title'] 
    char.male =row['male'] 
    char.culture =row['culture'] 
    char.dateOfBirth =row['dateOfBirth'] 
    char.DateoFdeath =row['DateoFdeath'] 
    char.mother =row['mother'] 
    char.father =row['father'] 
    char.heir =row['heir'] 
    char.house =row['house'] 
    char.spouse =row['spouse'] 
    char.book1 =row['book1'] 
    char.book2 =row['book2'] 
    char.book3 =row['book3'] 
    char.book4 =row['book4'] 
    char.book5 =row['book5'] 
    char.isAliveMother =row['isAliveMother'] 
    char.isAliveFather =row['isAliveFather'] 
    char.isAliveHeir =row['isAliveHeir'] 
    char.isAliveSpouse =row['isAliveSpouse'] 
    char.isMarried =row['isMarried'] 
    char.isNoble =row['isNoble'] 
    char.age =row['age'] 
    char.numDeadRelations =row['numDeadRelations'] 
    char.boolDeadRelations =row['boolDeadRelations'] 
    char.isPopular =row['isPopular'] 
    char.popularity =row['popularity'] 
    char.isAlive =row['isAlive'] 

    db.session.add(char)
    db.session.query(CharacterPredictions).all()

db.session.commit()
