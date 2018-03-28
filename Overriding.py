class Animal:

  def dog(self):
    print("dog is Eating")

class Animal1(Animal):
  def dog(self):
    print("dog is barking")

d=Animal1()
d.dog()
