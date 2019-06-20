class Bear:
	def sound(self):
		return "Groarrr"

class Dog:
	def sound(self):
		return "Woof woof!"

class Animal:
	def makeSound(self, animal):
		return animal.sound()
