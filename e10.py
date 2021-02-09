list1= [1,2,3,4,5,6,7,8,9]
list2=[1,1,1,10,4,5,20,4,20,30,40,50]
new=[]
for i in list1:
    if i in list2:
        new.append(i)
print(new)

#create or generate a two list and then return a neww list which have contain commom numbers (without duplicate).
