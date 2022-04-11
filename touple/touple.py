# touple is the data type in python
# we can create touple by using round bracket
#in touple we can able to add repettative value, that is duplicate value, touple is ordered data strcuture
#touple can be use to store data 
#touples are indexed first item is 0 postion second is 1 as so on
#when we see tuple is order its mean order of the items defined and order of item will not change
#tuple are unchangebale means we can not add, update value in tuple after tuple crated.

#tuple are indexed hence allow duplicate value

tuple = (1,3,4,4,4,4,3,3,3,3)
print(tuple)

#length of tuple 
print(len(tuple))

#create tuple with one item
#when we create any tuple with round brack most important is to give comma (,)
#if we not give any commat to tuple then it will consider as string data type

tuple = ("shubham")
print(type(tuple))
tuple= ("shubham",)
print(type(tuple))

#tuple data type
#tuple can able to sotre any data type 

tuple = (11,3,3,3,3,"shubham",3.33)
print(tuple)
print(type(tuple))

#how can we create touple with constructon
#tuple1=tuple((22,3,3,3,3,33,3))   #note that double round brack is necessary for tuple
#print(type(tuple1))

#accessing tuple item by using indexing

print((tuple[1]))

#change Tuple value to change tuple value we need to first convert tuple into list then  we need 
#perform list operation tuple

#x = ("apple", "banana", "cherry")
#y = list(x)
#y[1] = "kiwi"
#x = tuple(y)
#
#print(x)
#add tuple to tuple we can add Item in tuple by usig two way one is by using convert into listand
#seond is the by using Additon operator create another tuple and add it with prevous one

x =("apple","macbook","hcer")
y=("red",)

x = x+y
print(x)

#How to remove element form tuple by using the  convert to list and pefrorm list operationn and get back to the tuple

#we can use del keywoard to delete the complete tuple 
#del x
#print(x)

#packing tuple
#packing of tuple means when we assgine value to tuple its know as packing
shubham = ("hsubha","shdjf")
#but in python there also unpacking option we can also able extract value back to variable its called unpacking

fruits = ("apple","orange","leamnon")
(red,yellow,blue) = fruits
print(blue)

student = ("Akash","ravi","puja","tanvi")

(mathtopper,sciencetopper,physicstopper,chemistrytopper) = student

print(mathtopper)
#using asteric * packing unpacking
#if the number of value is less then the number of variable then we give * sign to last value or
#any middle it will take postion of all value that having left in our tuple
#
Items = ("Mobile","cloth","vechcal","dange")

(electronic,accesories,*car) = Items
print(car)
#in middle astric *
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#loop through the touple
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
for i in fruits:
    print(i)
print("loop end")
#we can also use for loop on tuple by using index number of the tuple
for i in range(len(fruits)):
    print(fruits[i])

# we can also use while loop on tuple by using i
print("while loop started")
i = 0 
while i < len(fruits):
    print(fruits[i])
    i=i+1

i = 0
while i <len(fruits)-2:
    print(fruits[i])
    i = i+1



temp = fruits.count("apple")
print(temp)
print(fruits.index("apple"))