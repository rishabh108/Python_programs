class Animal:
    def __init__(self):
        print("This is Animal")

class dog(Animal):
    def eat(self):
        print('Eating')

class dog1(dog):
    def bark(self):
        print('barking')
class weep (dog1):
    def weep(self):
        print('Weeping')
d = weep()
d.eat()
d.bark()
d.weep()