class Entry:
	def __init__(self, priority, value):
		self.priority = priority
		self.value = value
	def set_priority(self, priority):
		self.priority = priority
	def get_priority(self):
		return self.priority
	def get_value(self):
		return self.value
	def __str__(self):
		return "Priority: " + str(self.priority) + "; Value:" + str(self.value)
		
class PQ:
	def __init__(self):
		self.list = []
	def add(self, priority, value):
		self.list.append(Entry(priority, value))
	def remove_min(self):
		#list to append the priority values to
		temp=[]
		#append these priority values to the temp list
		for item in range(len(self.list)):
			temp.append(self.list[item].priority)
		#return the value that is going to be removed
		returnValue = self.list[temp.index(min(temp))]
		#remove the min value from the pq list
		self.list.remove(self.list[temp.index(min(temp))])
		#remove the minimum from the temp list
		temp.remove(min(temp))
		#return the value that is removed
		return returnValue
		
	def set_priority(self, value, priority):
		for item in self.list:
			if(item.value == value):
				item.priority = priority
	def size(self):
		return len(self.list)

pq = PQ()
pq.add(2, "Eat")
pq.add(0, "Study for CS 3035")
pq.add(3, "Sleep")
pq.add(1, "Maintain Personal Relationships")
pq.add(4, "Practice Good Personal Hygiene")
pq.set_priority("Practice Good Personal Hygiene", 2)
pq.set_priority("Eat", 4)


while pq.size() > 0:
	print(pq.remove_min())
