from random import random
from queue import Queue
import threading
import time
import datetime
import sys

class Pancake:
	pancakeCount = 0
	def __init__(self):
		Pancake.pancakeCount += 1
		self.pancakeCount = Pancake.pancakeCount
	def __str__(self):
		return " Pancake #" + str(self.pancakeCount)

class Cook:
	def __init__(self, name, pancakeStack):
		self.name = name
		self.pancakeStack = pancakeStack
	def cook_pancake(self):
		pancake = Pancake()
		print(self.name + " the cook cooks" + str(pancake))
		return pancake
	def work(self):
		print(self.name + " goes to work")
		while True:
			self.pancakeStack.put(self.cook_pancake())
			time.sleep(int(random()*2))
	def __str__(self):
		return self.name + " the cook"
		
class Customer:
	def __init__(self, name, pancakeStack):
		self.name = name
		self.pancakeStack = pancakeStack
	def eat_pancake(self, pancake):
		print(self.name + " the customer eats" + str(pancake))
	def dine(self):
		print(self.name + " eats")
		while True:
			if self.pancakeStack.empty():
				print("No pancakes ready to eat")
			else:
				print(str(self.pancakeStack.qsize()))
				pancake = self.pancakeStack.get()
				self.eat_pancake(pancake)
				self.pancakeStack.task_done()
			time.sleep(int(random()*3))
	def __str__(self):
		return self.name + "is eating"
		
class PancakeHouse:
	def __init__(self):
		self.pancakeStack = Queue()
		self.listOfCooks = []
		self.listOfCustomers = []
	def add_cook(self, name):
		cook = Cook(name, self.pancakeStack)
		self.listOfCooks.append(cook)
	def add_customer(self, name):
		customer = Customer(name, self.pancakeStack)
		self.listOfCustomers.append(customer)
	def begin_shifts(self):
		for cook in range(len(self.listOfCooks)):
			cook_thread = threading.Thread(target = self.listOfCooks[cook].work, daemon = True, args = ())
			cook_thread.start()
	def serve_customers(self):
		for customer in range(len(self.listOfCooks)):
			customer_thread = threading.Thread(target = self.listOfCustomers[customer].dine, daemon = True, args = ())
			customer_thread.start()
	def open(self, length):
		start = datetime.datetime.now().timestamp()
		self.begin_shifts()
		self.serve_customers()
		time.sleep(length)
		print(str(self.pancakeStack.qsize()) + " uneaten pancakes")
		while self.pancakeStack.qsize() > 0:
			print(self.pancakeStack.get())
		sys.exit()
	def __str__():
		return "Welcome to the pancake house!"
def driver():
	pancakeHouse = PancakeHouse()
	pancakeHouse.add_cook("Dexter")
	pancakeHouse.add_cook("Paul")
	pancakeHouse.add_customer("ObiWan")
	pancakeHouse.add_customer("John")
	pancakeHouse.open(6)
driver()
