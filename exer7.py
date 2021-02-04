#Question 9: Reverse a given number and return true if it is the same as the original number

def reverse(num):
    num=str(num)
    if num==num[::-1]:
        print(num,"number is same in reverse")
    else:
        print("not same")

reverse(121)