# factorial of the number...
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print("facoroal is ", fact(5))
