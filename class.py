#!/usr/bin/env python
class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        print "Generic Animal sound"

animal = Animal("thing")
animal.talk()

class Cat(Animal):
    def talk(self):
        print '%s says, "Meow!!"' % (self.name)

cat = Cat("Groucho")
cat.talk()

class Cheetah(Cat):
    def talk(self):
        print "Growl !!!"

cheetah = Cheetah("xxx")
cheetah.talk()

