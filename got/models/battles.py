from sqlalchemy import Column, Integer, String, Boolean
from got import db

class Battles(db.Model):
	id = Column(Integer, primary_key=True)
	name = Column(String)
	year = Column(String)
	battle_number = Column(String)
	attacker_king = Column(String)
	defender_king = Column(String)
	attacker_1 = Column(String)
	attacker_2 = Column(String)
	attacker_3 = Column(String)
	attacker_4 = Column(String)
	defender_1 = Column(String)
	defender_2 = Column(String)
	defender_3 = Column(String)
	defender_4 = Column(String)
	attacker_outcome = Column(String)
	battle_type = Column(String)
	major_death = Column(String)
	major_capture = Column(String)
	attacker_size = Column(String)
	defender_size = Column(String)
	attacker_commander = Column(String)
	defender_commander = Column(String)
	summer = Column(String)
	location = Column(String)
	region = Column(String)
	note = Column(String)

    
    def __iter__(self):
        yield 'id', self.id
        yield 'name', self.name
        yield 'battle_number', self.battle_number
        yield 'defender_king', self.defender_king
        yield 'attacker_1', self.attacker_1
        yield 'attacker_2', self.attacker_2
        yield 'attacker_3', self.attacker_3
        yield 'attacker_4', self.attacker_4
        yield 'defender_1', self.defender_1
        yield 'defender_2', self.defender_2
        yield 'defender_3', self.defender_3
        yield 'defender_4', self.defender_4
        yield 'attacker_outcome', self.attacker_outcome
        yield 'battle_type', self.battle_type
   		yield 'major_death', self.major_death
        yield 'major_capture', self.major_capture  
        yield 'attacker_size', self.attacker_size
        yield 'defender_size', self.defender_size
        yield 'attacker_commander', self.attacker_commander
        yield 'defender_commander', self.defender_commander
        yield 'summer', self.summer
        yield 'location', self.location
        yield 'region', self.region
        yield 'note', self.note