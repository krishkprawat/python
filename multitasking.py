from threading import Thread, current_thread, Lock

class Flight:
    def __init__(self, available_seats):
        self.available_seats= available_seats
        self.l=Lock()

    def reserve(self,need_seat):
        self.l.acquire(blocking=True, timeout=1)
        print("available : " ,self.available_seats)
        if (self.available_seats>=need_seat):
            name=current_thread().name
            print(f'{need_seat} is allotted to {name}')
            self.available_seats -= need_seat
        else:
            print("sorry seats are full.")
        self.l.release()

f= Flight(5) #available sets are 5
t1= Thread(target= f.reserve,args=(1,),name='krish') #t1 need  seat
t2= Thread(target= f.reserve,args=(6,),name='vijay') # t2 need 6 seat

t1.start()
t2.start()






