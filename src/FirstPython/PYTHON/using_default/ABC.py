class Animal :
    def eat(self):
        return "eating"

class Walker :
    def walk(self):
        print('walking')

class Running :
    def run(self):
        print('running')

class Dog(Animal,Walker,Running):
    def bark(self):
        print('barking')

dog=Dog()

print(dog.bark())
print(dog.eat())
print(dog.walk())
dog.run()