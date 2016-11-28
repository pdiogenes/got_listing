from sqlalchemy import Column, Integer, String, Boolean, Numeric
from got import db


class CharacterPredictions(db.Model):
    S_No = Column(Integer, primary_key=True)
    actual = Column(Integer)
    pred = Column(Integer)
    alive = Column(Numeric(precision=4, scale=3))
    plod = Column(String)
    name = Column(String)
    title = Column(String)
    male = Column(String)
    culture = Column(String)
    dateOfBirth = Column(Integer)
    DateoFdeath = Column(Integer)
    mother = Column(String)
    father = Column(String)
    heir = Column(String)
    house = Column(String)
    spouse = Column(String)
    book1 = Column(Integer)
    book2 = Column(Integer)
    book3 = Column(Integer)
    book4 = Column(Integer)
    book5 = Column(Integer)
    isAliveMother = Column(Integer)
    isAliveFather = Column(Integer)
    isAliveHeir = Column(Integer)
    isAliveSpouse = Column(Integer)
    isMarried = Column(Integer)
    isNoble = Column(Integer)
    age = Column(Integer)
    numDeadRelations = Column(Integer)
    boolDeadRelations = Column(Integer)
    isPopular = Column(Integer)
    popularity = Column(Numeric(precision=16, scale=15))
    isAlive = Column(Integer)
    
    def __iter__(self):
        yield 'S_No', self.S_No
        yield 'actual' , self.actual
        yield 'pred' , self.pred
        yield 'alive', self.alive
        yield 'plod', self.plod
        yield 'name', self.name
        yield 'title', self.title
        yield 'male', self.male
        yield 'culture', self.culture
        yield 'dateOfBirth' , self.dateOfBirth
        yield 'DateoFdeath' , self.DateoFdeath
        yield 'mother', self.mother
        yield 'father', self.father
        yield 'heir', self.heir
        yield 'house', self.house
        yield 'spouse', self.spouse
        yield 'book1' , self.book1
        yield 'book2' , self.book2
        yield 'book3' , self.book3
        yield 'book4' , self.book4
        yield 'book5' , self.book5
        yield 'isAliveMother' , self.isAliveMother
        yield 'isAliveFather' , self.isAliveFather
        yield 'isAliveHeir' , self.isAliveHeir
        yield 'isAliveSpouse' , self.isAliveSpouse
        yield 'isMarried' , self.isMarried
        yield 'isNoble' , self.isNoble
        yield 'age' , self.age
        yield 'numDeadRelations' , self.numDeadRelations
        yield 'boolDeadRelations' , self.boolDeadRelations
        yield 'isPopular' , self.isPopular
        yield 'popularity' , self.popularity
        yield 'isAlive' , self.isAlive
