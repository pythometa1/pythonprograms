#list is use to store multiple input in single variable we can define list with square bracket
#list allow multiple type data
#list Items are order, changeable and duplicate can be we store
#list items are indexed and first item is count as list[0] second item as list[1]
#when we say list is ordered it means list element is in one order its not change when we add new e
#it goes to the end of the list There are some pre method that can able to change order 
#list is changebale that means we can change elements in list we can add ,delete 
#list allowed duplicates
#for find length of string we use len() to find
#list can be store any data type
#list typeof is as per python prespective its object with data type list
#

from math import e


list =[1,3,3,3,"shubham",3,3]
print(list)
print(len(list))

#python access list ITEMs
#list items are indexed and we can access it through index

print(list[2])
print(list[0:4])

print(list[-4:])

#change list value
list[1] = "love"
print(list)
list[1:3] ="loveis","blind"
print(list)

#insert Item into list with out replacing any value of the list by using insert() in insert there or any postion

x = "shubham"
list.insert(1,"shubhm")
print(list)


y = "radha"
list.insert(4,y)
print(list)

z = "manisha"
list.insert(4,z)
print(list)

r = "virat"
list.insert(1,r)
print(list)

#append value into the list append use to add value into the list at the end of the list

friend = "akash","ravi","varad"
for i in friend:
    list.append(i)
print(list)

Marks = 13,3,23,3,23,23
for i in Marks:
    list.append(i)
print(list)

#extend() the list these function is use for to add two list into one
friends =[1,3,3,3,3,3,3,"shubham",'is']
love = ["is","good","boy"]

friends.extend(love)
print(friends)

marriage = ["sh","is","good","boy"]
friends.extend(marriage)
print(friends)
m = [1,3,3,3,3,3]
Mar = ("sh","ah","um","ud")
m.extend(Mar)
print(m)

superhero = ["shaktiman","powerRanger","junierG"]
#remove key woard is use to remove specic value thorough name of value
superhero.remove("shaktiman")
print(superhero)
#pop() method is use to remove value through specific key
superhero.pop(1)
#if we not give any value into pop it remove last element

print(superhero)

#loop through the list by using for loop
list = [2,3,3,4,34,34,4]
for i in list:
    print(i)
#loopt through the index value of the list
list =["shubham","is","good","boy"]

for i in range(len(list)):
    temp = 0
    temp = temp+1
    print(list[i])
    print(temp)
#itreate on list using while loopp
print("while loop")

m= 0
while m < len(list):
    print(list[m])
    m= m+1
    
list1 = ["shubham","yeljale","is"]

i = 0
while i<len(list1):
    print(list1[i])
    i= i+1
print(i)

listm= ["kirana","store","is","avilable","fordaily"]

i = 0 
while i < len(listm):
    print(listm[i])
    i = i+1
print(i)

[print(x) for x in list]
[print(x) for x in listm]
[print(x) for x in listm]
[print(x) for x in listm]
    
#comparision in list

list =["shubham","yeljale","is","best","programer","in","world"]
temp = []
for i in range(len(list)):
    if "shubham" in list:
        temp.extend(list)
print(temp)
    
x=[y.upper() for y in list]
print(x)
 
z =[r.casefold() for r in list]
print(z)

m = list.sort()
print(list)

#list sorting Alphanumerical
m =[]

list = [1,3,3,3,4,5,66,6,6,54,43,24,23]
m = list.copy()
m.sort()
print(m)
print(list)

#sort list in ascending order
list1 = [3,3,3,3,4,44,555,54,3,2,3,3,2,3,3,23,3]
list1.sort(reverse = False)
print(list1)

#you can write function for sort list

def myfunc(n):
    return abs(n-50)


list1.sort(key = myfunc)
print(list1)


#print value that near by 555
def myfunct(n):
    return abs(n-555)
list1.sort(key = myfunct)
print(list1)

#Case insensitive

list11 =["SHUBHAM","yeljale","rajge","is","DON","IS","HERE"]
list11.sort()
print(list11)

list111 =["shubham","is","good","3323","jare"]
list111.sort(key = str.upper)
print(list111)

list111.reverse()
print(list111)

#copy one list to another list

lis2 = [2,3,3,3,3,3,333]
lis1 = lis2.copy()



#join two list using + operator

str = ["shubham","ravi","Akash"]
prem =["Yeljale","Pawar","satre"]
strr = str + prem
print(strr)
#another option is append lis2 element into list one one by one

for i in prem:
    str.append(i)
print(str)