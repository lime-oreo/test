from abc import ABC, abstractclassmethod

#추상 클래스 정의
class Animal (ABC):
    @abstractclassmethod
    def make_sound(self ):
        pass
    def sleep (self):
        print("The animal is sleeping")

class Dog (Animal):
    def make_sound(self):
        print('Bark!')
class Cat(Animal):
    def make_soung(self):
        print("Meow!")

dog= Dog()
cat = Cat()

dog. make_sound()
cat.make_sound()

dog.sleep()
cat.sleep()

        


