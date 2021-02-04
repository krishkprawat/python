class Fruit:
    #def __init__(self):
        #print("i am parent constructor")
    def apple(self):
        print("i am apple in the fruits")

class Drinks:
    def apple(self):
        print("i drinks clas apple")

class Chips(Fruit,Drinks):  #mro method  resolution order ----> if class chips inherit two class then it inherit only firstly write parent class
    #means only inherit fruits classs.
        print("i am chips")


c= Chips()
c.apple()

        