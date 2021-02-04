class Student:
    def __init__(self, name, school):
        self.name=name
        self.school=school
    
    def info(self):    # this is method 
        print( self.name)
        print( self.school)

s=Student("vijay","rdsvm")
s2= Student("krish","timli")
s.info()
s2.info()

    