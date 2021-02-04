#from threading import Thread
#def disp():
 #   pass
#t=Thread(target=disp, name="krish thread")
#print(t.name)



#or secod way--->
from threading import Thread
def disp():
    pass
t=Thread(target=disp)

t.setName("krish thread new")
print(t.getName())
