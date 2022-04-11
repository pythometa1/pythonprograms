#python having following Data type
#text = str
x = "sshubham"   # x = str("shubham")
print(type(x)) 
#Numeric type = int,float,complex
y = 23       #y = int(23)
z=23.3        #z =float(23.3)
e = x+3j      #e =complex(x+3j) We can not convert compleax number into another datatype
#sequence type = list,tuple,range
list =[1,3,3,4,23,23,3]   #x = list[23,3,3,3,3,]
tuple =(3,4,23,23,23,3)   #y = tuple(3,3,3,3,3,3)
z = range(7)
#Mapping type = Dict
shubham = {"a":34,"b":34}  #x = dict{"as":3,"b":3}
#set type = Frozenset, set
set = (1,3,4,5,6,2) 
frozenset = ({"shubham","yeljale","is"})
#boolean type = Bool
x = True ,False
#binary type = bytes, bytes array , memory view
bytes =b"hello"
bytes_array =bytearray(4)
Memoryview = memoryview(bytes(3))

#python casting done by using contructor function  for example int() in int it remove all decimal point float() str()