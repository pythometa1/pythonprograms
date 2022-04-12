#set is data type in python
#it defined by using {} bracket
# set is data type that non changable, non updatable and un ordered, un indexed data type

example ={"shubham","yelja;e","is"}
print(type(example), example)


#shubham

#set is unorder so we can not predict in which order set will come
#set Item are unorder,unchangeable , and not allowed duplicate value if it found duplicate value it should be remove automatically
example = {"shubham","shubham","is"}
print(example)
#unordered set is unordered means its not defined and indexed every it change order by its self
#unchangable means we can not add or delete element after set created
#set can be able to take any data type we can find lenth of using len()
example ={True,False,"shubham",2,3}
print(example)

# we can make set by using set() constructor

example = set(("shubham",True,2))
print(type(example))

#When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.


#access Item ins set using for loop we can not access set item by using index value but for loop
#we can acceess, and we can also find element in set is that present or not

kiran ={"sugar","rice","fish","meat"}
for i in kiran:
    print(i)

if "kkk" in kiran:
    print("Yes its present")
else:
    print("not prest")

    # Add items in set
#when we created set we can not changes its item but we can add item into set
#to add item in set we use add()

fruits ={"mango","apple","peru"}

fruits.add("Pinaple")
print(fruits)

#add items in set by using another set
# we can add any iterable object in set by using update method its not mandatory it should be as set
shoes =["hokey","jokey","leman"]

fruits.update(shoes)
print(fruits)
print(type(fruits))

#to remove ITEM form set we use remove method or discard method

fruits.remove("mango")
print(fruits)
#if item is not present in set then it wil raise Key error in remove method
#fruits.remove("mango")
print(fruits)

fruits.discard("hokey")
print(fruits)
#if the item remove not in fruits it will not raise any error
fruits.discard("hokey")
print(fruits)
#we can also use pop method to remove item form list but it will remove last element and
#set is unoarder data type so we don't know which element would be removed.

#clear method is use to clear complet set
fruits.clear()
print(fruits)

# Del key word delete the set completely 
del fruits

#Note: Both union() and update() will exclude any duplicate items.
#Join Two Sets
#There are several ways to join two or more sets in Python.
#You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another
shubham = {1,2,3,4,5,6,7}
raje = {8,9,10,11,12,1,32}
set = shubham.union(raje)
print(set)
# if we want to find common element in two sets the n we use instersection_update()

shubham.intersection_update(raje)
print(shubham)

set11 = shubham.intersection(raje)
print(set11)