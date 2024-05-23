from abc import ABC, abstractmethod
import math

class Cryptid():
	def __init__(self, name, height):
		self.name = name
		self.height = height
	@abstractmethod
	def attack(self, location):
		pass
	def __eq__(self, other):
		if((self.name == other.name) and (math.isclose(self.height,other.height))):
			return True
		else:
			return False

class Yeti(Cryptid):
	def __init__(self, name, height):
		self.name=name
		self.height = height
	def __str__(self):
		return self.name + " is " + str(self.height) + " meters tall"
	def attack(self, location):
		return self.name + " throws ice at the citizens of" + location
	def __add__(self, other):
		return Yeti(self.name+other.name, self.height+other.height)
	
		
monster = Cryptid("Crazy", 3.5)
monster2 = Cryptid("Crazy", 3.5)
print(monster==monster2)
difMonster = Yeti("Snow", 5.5)
difMonster1 = Yeti("Sand", 0.5)
print(difMonster==difMonster)
print(difMonster)
print(difMonster.attack("Tokyoyo"))
print(difMonster + difMonster1)
