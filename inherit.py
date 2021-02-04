class Animal:
    def __init__(self):
        print("animal created")

    def eat(self):
        print("i am eating")
    
class Dog(Animal):
    def __init__(self):
        super().__init__()   #super is calling parent constructor.
        print("its ddoggy.")

d=Dog()
d.eat()
