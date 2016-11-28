from sqlalchemy import Column, Integer, String, Boolean
from got import db

class CharacterDeaths(db.Model):
	id = Column(Integer, primary_key=True)
	name = Column(String)
	allegiances = Column(String)
	death_year = Column(Integer)
	book_of_death = Column(Integer)
	death_chapter = Column(Integer)
	book_intro_chapter = Column(Integer)
	gender = Column(Boolean)
	nobility = Column(Boolean)
	got = Column(Boolean)
	cok = Column(Boolean)
	sos = Column(Boolean)
	ffc = Column(Boolean)
	dwd = Column(Boolean)

	def __iter__(self):
		id = Column(Integer, primary_key=True)
		yield 'name', self.name
		yield 'allegiances', self.allegiances
		yield 'death_year', self.death_year
		yield 'book_of_death', self.book_of_death
		yield 'death_chapter', self.death_chapter
		yield 'book_intro_chapter', self.book_intro_chapter
		yield 'gender', self.gender
		yield 'nobility', self.nobility
		yield 'got', self.got
		yield 'cok', self.cok
		yield 'sos', self.sos
		yield 'ffc', self.ffc
		yield 'dwd', self.dwd