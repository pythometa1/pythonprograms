#string in python define by using the "" 
var = "shubham is goood boy"

#for multi line string python using """ shubham is good boy"""
var = """shubham is good boy"""

#string are arrays
#in many other programing langauge like pythonn having string sotored in array form
a = "shubham yeljale"
print(a[4])

# since string is array we can traverse loop through the stirng

for i in a:
    print(i)
#to find length of string we use len function

print(len(a))

#if we want to print particular phrase in string or same phrase in string then we use in Keyword

s = "shubham is good boy"
print("boy" in s)


if "good"  in s:
    print("good is present")
# check if not is 

if "good2" not in s:
    print("shubham is good")

#slicing: we can use slicing for to take some part of string for slicing we need to give starting part
# and endiing part parameter
a = "shubham is good boy"

aa=a[11:15]
print(aa)
#slice form stara
bb= a[:8]
print(bb)
#slice form end
cc=a[8:]
print(cc)
#use negative index for slicing
dd =a[-5:-3]
print(dd)
mm =a[-1]
print(mm)
#strip() remove white space form end and begaing

str = "   shubham yeljale"
str2 = "shubham"
print(str)
print(str.strip())
#uppercase
print(str.upper())
print(str.lower())
print(str.replace('h','y'))
print(str.split())
print(str+str2)
print(str+ " "+str2)

# by using format method we can combine integer and character
#the format() method takes integer and palace it to the positon of{}
#format method can take unlimeted number of argument

age =45
str= " my age is {}"
print(str.format(age))
km=93
marks = 23
str = "my marks {} age {} and km{}"
print(str.format(age,marks,km))
#we can use index {0} to ensure to check argument placed in right postion

#for insert double cote we use \" is \"
str = "shubha \" is \"good boy"
print(str)