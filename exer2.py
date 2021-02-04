#Question 2: Given a range of first 10 numbers, Iterate from start number to the end number and 
# print the sum of the current number and previous number

def sumnum(n):
    previous=0
    for i in range(n):
        sum=previous+i
        print("current number is", i,"previous number is :", previous, "sum is :",sum)
        previous=i

sumnum(10)