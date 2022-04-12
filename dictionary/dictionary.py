
#create Dictionary in python by using {}

dict = {"Shubham":"yeljale","ravi":"rana","ravi":"is"}
print(dict)
print(type(dict))

#dictonary is data type its allowed to store value 
#its orderd form3.7 before that its un ordered
#dictionary ordered ,changeable, and not allowed duplicate in dictionary
#dictionary return in key value pair with curly braces {}
#dictionary ITem refree through the Key

print(dict["Shubham"])
print(dict.keys())

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

#for remove element form dictionary pop method is use popitem() remove last element of dictionary
thisdict.pop("brand")
print(thisdict)

# Loop through dictionary:
# when we print Key of dictionary then we just need to pass i through the loop
# when we print value of the dictionar then we nnedd to give dictionary name of i
#we can also print dictionary value using value()
for i in thisdict:
    print(thisdict[i])
for i in thisdict.values():
    print(i)

#for return keys of the dictionary we use Keys() 
for i in thisdict.keys():
    print(i)

# by using items() we can print both key and values
for i,k in thisdict.items():
    print(i,k)

for i,j in thisdict.items():
    print(i,j)


#copy Dictionary 

# we can not made dictionary copy by simply assgine = sign to dictionary if we assgine that then
#it will change second dictionary value to the first one 
#for copy dictionary in in dictioary the is method that name is copy()
#lets create two dictionary 
s = {"1839532":"shubham yeljale","12343":"RADHIKA","23434":"RUPESH"}
M = {"23433":"radhika sawant", "23434":"priya Pawar"}

s.copy()
s1 = M.copy()
print(s1)
#mydict = dict(s)