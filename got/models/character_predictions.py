from sqlalchemy import Column, Integer, String, Boolean
from got import db


class (db.Model):
    S_No = Column(Integer, primary_key=True)
    actual = Column(Integer)
    pred = Column(Integer)
    alive = Column(String)
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
    popularity = Column(Integer)
    isAlive = Column(Integer)
    
    def __iter__(self):
        yield 'id', self.id
        yield 'num', self.num
        yield 'name', self.name
        yield 'type1', self.type1
        yield 'type2', self.type2
        yield 'total', self.total
        yield 'hp', self.hp
        yield 'attack', self.attack
        yield 'defense', self.defense
        yield 'sp_atk', self.sp_atk
        yield 'sp_def', self.sp_def
        yield 'speed', self.speed
        yield 'generation', self.generation
        yield 'legendary', self.legendary