import controllers.Polymorphism as pol

dog = pol.Dog()
bear = pol.Bear()

animal = pol.Animal()
print(animal.makeSound(dog))
print(animal.makeSound(bear))
