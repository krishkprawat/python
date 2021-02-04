#remove specific element in list.

list=[10,2,0,3,0,40,50]
e=0
if (e in list):
    list.remove(e)
else:
    print("element not found")

#enter element in list by 4 times.

list=[]
for i in range(4):
    e=int(input("enter element: "))
    list.append(e)

print(list)


#print second largest in list------------>>

l=[10,2,30,400,55,61]
l.sort(reverse=True)
print(l[1])

#count all char in word=-=---->>

word="facebookvscode"
dict={}
for key in word:
    if key in dict:
        dict[key]+=1
    else:
        dict[key]=1
print(dict)




