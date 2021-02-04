class Student:
    def __init__(self, name , roll): # name and roll are normal variables.
        self.name=name
        self.roll=roll  #variables with self keyword are instance variable under the classs.

s=Student("krishnapal",100)
print(s.name, s.roll)

#self.name= current object name. self refers to current object.