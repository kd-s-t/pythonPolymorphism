class Bear:
	def sound(self):
		print("Groarrr")
 
class Dog:
	def sound(self):
		print("Woof woof!")

class Animal:
	def makeSound(self, animal):
		animal.sound()

dog = Dog()
bear = Bear()

animal = Animal()
animal.makeSound(dog)
animal.makeSound(bear)