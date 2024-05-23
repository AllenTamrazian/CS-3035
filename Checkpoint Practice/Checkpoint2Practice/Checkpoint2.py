import sys
class Monster:
	def __init__(self, name, size):
		self.name = name
		self.size = size
		
	def attack(self, location):
		print(self.name + " attacks " + location)
		
	def getName(self):
		return self.name

	def getSize(self):
		return self.size
		
	def setSize(self, size):
		self.size = size
	
	def setName(self, name):
		self.name = name
		
	def __str__(self):
		return "The monster is named " + self.name + " and has a size of " + str(self.size)
		
	def __eq__(self, other):
		if((self.name == other.name) and (self.size == other.size)):
			return True
		else:
			return False

	def __add__(self, other):
		return Monster("" + self.name + other.name, self.size + other.size)

def main():
	#1 __init__ method
	firstMonster = Monster("Godzilla", 10)
	secondMonster = Monster("Mothra", 10)
	#2 __str__ method
	print(firstMonster)
	#3 setSize method
	secondMonster.setSize(7)
	#4 getSize method
	print("Size of second monster: " + str(secondMonster.getSize()))
	#5 __eq__ method
	print(firstMonster==secondMonster)
	#6 attack method
	firstMonster.attack("Tokyo")
	#7 __add__ method
	thirdMonster = firstMonster + secondMonster
	print(thirdMonster)
	
if __name__ == "__main__":
	sys.exit(main())
