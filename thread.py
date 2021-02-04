#from threading import Thread
#def disp(a):
 #   print("thread running",a)
#t= Thread(target=disp, args=(10,))
#t.start()


from threading import Thread
def disp():
    for i in range(5):
        print("child thread")
t= Thread(target=disp)
t.start()     #from line 9 to 12 this is child thread which is start when call start().


for i in range(5):
    print("parent threadd")  #main thread