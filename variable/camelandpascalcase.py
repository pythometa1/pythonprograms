#camel case - Each word except first word start with capital
#for example = FedEx,WordPerfect
var = "Fedex"

#Pascal case = in pascal case Need every letter start with capital while in camel case is simlar to 
#pascal but differnce is camel no need to write first letter capital

var = "ShubhamYeljale"

#snake case is Each word use underscore with space
var ="shubham_yeljale_is_good"

#python assgine multiple value to multiple variable Many Values to Multiple Variables

x,y,z = "shubham","yeljale","don"

print(x)
print(y)
print(z)
# One Value to Multiple Variables
x = y= z= "orange"
print(z)
print(y)

#Unpack a Collection If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple","Mango","banana"]
x,y,z=fruits
print(x)
print(z)

#Output Variables
#print function is use to multiple output
s = "shubham"
print(s)

#print multiple output with sepratedwith comea
x = "shubham"
y="raje"
z="danger"
print(x,y,z)

#Global variable :
#The function that created outside the function is called as global variable
#if you created variable inside the function it will treat as local variable can only be used
#inside the function the global variable remain same as it treated as global if local having same name

var = 19
def additon():
    a=20
    x=a+var
    print(x)
print(additon())

#If you want to create any variable inside the function that you want to access it globally
#then that time you need to give that variable name is global and variable name and value
#if you want to change value of the global key word inside the function then use global keywoard
def Globalvariable():
    global varm
    varm = "shubham"

    print(varm)
#capitalize make first latter to capital
str = "SSShubham 1 is good boy"
print(str.capitalize())
#case fold make string to small case
print(str.casefold())
#centre  method take two argument and first for size and align it to cente
print(str.center(20,"0"))
#count is take one argument and find how many arguments in same like in string if they found return number of that argumen

print(str.count("is"))
#find keyword would help to find postion of the character form start
print(str.find("i", 10,1))
#format_map Jr aplyal eknda array mde value dila asting ter tya direct apn takus shito

s ={"x":"1","y":"3","z":"3"}
print("{x},{y},{z} is good".format_map(s))

#if string is in lower case then it will return TRUE value Else return False value
print(str.islower())
#if string all charater is numberic then it will return TRUE
print(str.isnumeric())
#isupper() return True if all character in string in upper case
print(str.isupper())
#.join() that method is use to replace whitespace, comma, lot or any value that given into in fucntion

shubham =( "shubham", "is", "good", "booy")
shh = '#'.join(shubham)
print(shh)

shubham =["shubham yeljlae is good boy"]
shhe= " ".join(shubham)
print(shhe)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)
#Note: When using a dictionary as an iterable, the returned values are the keys, not the values.
mddict = {"name":"shubham","yeljale":"yeisl","don":"bhai"}
mysepratori = "*"
x = mysepratori.join(mddict)
print(x)
#join()  ** replace krt comma sobat but tya sthi applyala "" string type data lgto
list = ["1","2","3"]
oper="**"
xy = oper.join(list)
print(xy)
#maketranse() for make transe we need to give two argument in method what we want to change with resepctive what we change
#maketranse store in one variabel and that variable need to the pass translate()
puja = "puja is good girl than radha"
x = puja.maketrans("p","u")
print(puja.translate(x))

sanskruti = "sanskruti is best girl in the world"
x = sanskruti.maketrans("is","in")
print(sanskruti.translate(x))
#partition () is use to divide string into three part if give first value it will crate emptystring

print(sanskruti.partition("sanskruti"))

#split() split function use mostly list mde conversion krnya sthi hot string che

list ="my name is gooogle and am able to redd"
print(list.split(" "))

txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)

t = "apple,is,good,boy,than,me,never"
x= t.split(",")
print(x)
#jr aplyalla khii pramant ch list krychi asen ter apn value pn taku shakto
m = "shubham#is#god#boy#HHE#HKJ##"
x=m.split("#",5)
print(x)
#strip() when we want to send value string in between then we use strip method
txt = "banana"
x = txt.strip()
print("of all fruits", x, "is my favorite")

mxt = "shubham is good boy"
z= mxt.strip()
print("all shubham is",z, "hey")

txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)

#swapcase() if wor id capital it will convert to small or if samll it convert to large

Tse = "MY NAME is SHUBHAM"
mm = Tse.swapcase()
print(mm)
#title() its convert all word first letter to capital

tse = "shubham is good boy"
mmm= tse.title()
print(mmm)
#convert all letter into upper case 
uuu= tse.upper()
print(uuu)
#The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.

#If the value of the len parameter is less than the length of the string, no filling is done.
txt = "50"
x = txt.zfill(10)
print(x)