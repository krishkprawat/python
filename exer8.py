#fibonacci 0 1 1 2 3  5 8 13
def fib(n):
     a,b=0,1
     while a<n:
         print(a,end='')
         a,b=b, a+b

fib(10)


#another loop
number=int(input("enter the number : "))
i=0
x=0
y=1
while i<=number:
    print(i, end=' ')
    z=x+y
    x,y=y,z
    i+=1
