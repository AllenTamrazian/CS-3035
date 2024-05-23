from abc import ABC, abstractmethod

class SinglyLinkedListNode:
	def __init__(self, value, nextNode):
		self.value = value
		self.nextNode = nextNode
	def __str__(self):
		return "The value is: " + str(self.value)
	def setValue(self, value):
		self.value = value
	def setNextNode(self, nextNode):
		self.nextNode = nextNode
	def getValue(self):
		return self.value
	def getNextNode(self):
		return self.nextNode
class SinglyLinkedList:
	def __init__(self, firstNode, lastNode):
		self.firstNode = firstNode
		self.lastNode = lastNode
		self.length = 0
	def getFirstNode(self):
		return self.firstNode
	def getLastNode(self):
		return self.lastNode
	def addFirstNode(self, value):
		if(self.firstNode == None and self.lastNode == None):
			newFirstNode = SinglyLinkedListNode(value, self.firstNode)	#__init__() for SinglyLinkedListNode
			newFirstNode.nextNode = None
			self.firstNode = newFirstNode
			self.lastNode = newFirstNode
			self.length = self.length + 1
		else:
			newFirstNode = SinglyLinkedListNode(value, self.firstNode)
			newFirstNode.nextNode = self.firstNode
			self.firstNode = newFirstNode
			self.length = self.length + 1
	def addLastNode(self, value):
		if(self.firstNode == None and self.lastNode == None):
			newLastNode = SinglyLinkedListNode(value, self.lastNode)
			self.firstNode = newLastNode
			self.lastNode = newLastNode
			self.length = self.length + 1
		else:
			newLastNode = SinglyLinkedListNode(value, self.lastNode)
			self.lastNode.nextNode = newLastNode
			self.lastNode = newLastNode
			self.length = self.length + 1
	def deleteFirstNode(self):
		if(self.firstNode != None and self.lastNode !=None):	
			if(self.length == 1):
				self.firstNode = self.firstNode.nextNode
				self.lastNode = self.lastNode.nextNode
				self.length = self.length - 1
			else:
				self.firstNode = self.firstNode.nextNode
				self.length = self.length - 1
		else:
			print("Delete first node couldn't be done.")
	def deleteLastNode(self):
		if(self.firstNode != None and self.lastNode !=None):
			if(self.length == 1):
				self.firstNode = self.firstNode.nextNode
				self.lastNode = self.lastNode.nextNode
				self.length = self.length - 1
			else:
				current = self.firstNode
				count = 0
				while(count < self.length-2):
					current = current.nextNode
					count = count + 1
				current.nextNode = None
				self.lastNode = current
				self.length = self.length - 1
		else:
			print("Delete last node couldn't be done.")
	def __len__(self):
		return self.length
	def traverse(self):
		current = self.firstNode
		count = 0
		print("Traversing:")
		while (count < self.length):
			print(str(current) + " ")
			current = current.nextNode
			count = count + 1

class AbstractQueue(ABC):
	@abstractmethod
	def offer(self, obj):
		pass
	@abstractmethod
	def poll(self):
		pass
	@abstractmethod
	def peek(self):
		pass
	@abstractmethod
	def length(self):
		pass
		
class PythonListQueue(AbstractQueue):
	def __init__(self):
		self.list = []
	def offer(self, obj):
		self.list.append(obj)
	def poll(self):
		if(self.length() >= 1):
			returnValue = self.list[0]
			del self.list[0]
			return returnValue
		else:
			return "Nothing to poll"
	def peek(self):
		if(self.length() >= 1):
			return self.list[0]
		else:
			return "Nothing to peek"
	def length(self):
		return len(self.list)

class SLLQueue(AbstractQueue):
	def __init__(self):
		self.singlyLinkedList = SinglyLinkedList(None, None)
	def offer(self, obj):
		self.singlyLinkedList.addLastNode(obj)
	def poll(self):
		returnValue = self.singlyLinkedList.firstNode
		self.singlyLinkedList.deleteFirstNode()
		return returnValue
	def peek(self):
		if(self.length() >= 1):
			return self.singlyLinkedList.firstNode
		else:
			return "Nothing to peek"
	def length(self):
		return self.singlyLinkedList.length

def driver():
	print("\nSinglyLinkedList:")
	emptySinglyLinkedList = SinglyLinkedList(None, None)	#__init__() for SinglyLinkedList
	emptySinglyLinkedList.deleteFirstNode()	#deleteFirstNode()
	emptySinglyLinkedList.deleteLastNode()	#deleteLastNode()
	print("Length: " + str(emptySinglyLinkedList.length))	#__len__()
	print(emptySinglyLinkedList.getFirstNode())	#getFirstNode()
	print(emptySinglyLinkedList.getLastNode())	#getLastNode()
	emptySinglyLinkedList.traverse()	#traverse()

	notEmptySinglyLinkedList = SinglyLinkedList(None, None)
	notEmptySinglyLinkedList.addFirstNode(1)	#addFirstNode()
	notEmptySinglyLinkedList.traverse()
	notEmptySinglyLinkedList.addFirstNode(2)
	notEmptySinglyLinkedList.addLastNode(3)	#addLastNode()
	notEmptySinglyLinkedList.traverse()
	notEmptySinglyLinkedList.deleteFirstNode()
	notEmptySinglyLinkedList.deleteLastNode()
	notEmptySinglyLinkedList.traverse()
	print("Length: " + str(notEmptySinglyLinkedList.length))

	print("\nPythonListQueue:")
	#Empty PythonListQueue
	plq = PythonListQueue()	#__init__ for PythonListQueue
	print("plq length is: "+ str(plq.length()))	#length for PythonListQueue
	print(plq.peek())	#peek for PythonListQueue
	print(plq.poll())	#poll for PythonListQueue
	
	#Non empty PythonListQueue
	plq.offer(2)
	print("plq length is: "+ str(plq.length()))	#length for PythonListQueue
	print("Peek: " + str(plq.peek()))	#peek for PythonListQueue
	print("Poll: " + str(plq.poll()))	#poll for PythonListQueue
	print("Peek: " + str(plq.peek()))	#peek for PythonListQueue
	
	print("\nSLLQueue:")
	#Empty SLLQueue
	sllq = SLLQueue()	#__init__ for SLLQueue
	print("sllq length is: "+ str(sllq.length()))	#length for SLLQueue
	print(sllq.peek())	#peek for SLLQueue
	print(sllq.poll())	#poll for SLLQueue
	
	#Non empty SLLQueue
	sllq.offer(3)
	print("sllq length is: "+ str(sllq.length()))	#length for SLLQueue
	print("Peek: " + str(sllq.peek()))	#peek for SLLQueue
	print("Poll: " + str(sllq.poll()))	#poll for SLLQueue
	print("sllq length is: "+ str(sllq.length()))	#length for SLLQueue
	print("Peek: " + str(sllq.peek()))	#peek for SLLQueue
	
driver()
