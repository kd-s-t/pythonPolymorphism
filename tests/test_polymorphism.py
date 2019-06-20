import unittest
from controllers import Polymorphism

class TestPolymorphism(unittest.TestCase):

    def test_success(self):
        dog  = Polymorphism.Dog()
        bear = Polymorphism.Bear()

        animal = Polymorphism.Animal()
        dog_sound  = animal.makeSound(dog)
        bear_sound = animal.makeSound(bear)

        self.assertEqual(dog_sound, "Woof woof!")
        self.assertEqual(bear_sound, "Groarrr")

    def test_error(self):
        dog  = Polymorphism.Dog()
        bear = Polymorphism.Bear()

        animal = Polymorphism.Animal()
        dog_sound  = animal.makeSound(dog)
        bear_sound = animal.makeSound(bear)

        self.assertNotEqual(bear_sound, "Woof woof!")
        self.assertNotEqual(dog_sound, "Groarrr")
