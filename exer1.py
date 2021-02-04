#Question 1: Given a two integer numbers return their product and  if the product is greater than 1000, then return their sum


num1= int(input("first number is  :"))
num2= int(input("second number is  :"))
p= num1*num2
print("product is :",p)
if p>1000:
    print("sum is :" ,num1+num2)
    

