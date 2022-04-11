#operator is preform operation on variables
#there are servaral types of operator

#arthmetic operator
a = 20
b=23 
c1 = a+b  
c2 =a -b
c3= a*b
c4=a/b
c5=a%b
c7=a**b
c6=a//b
print(c1,c2,c3,c4,c5,c6,c7)


#assginment operator = ASSGINMENT OPERATOR IS USED TO ASSGINE VALUE TO VARIABLE
a =23
a=a+1 #a+=1
a= a&233
print(a)

#the table below: Let x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)

#Operator	        |            Meaning       	Example
#=======================================  |=======================
#&	Bitwise         |            AND	  |     x & y = 0 (0000 0000)
#|	Bitwise         |            OR	      |     x| y = 14 (0000 1110)
#~	Bitwise         |            NOT	  |     ~x = -11 (1111 0101)
#^	Bitwise         |            XOR	  |     x ^ y = 14 (0000 1110)
#>>	Bitwise         |            right    |    shift	x >> 2 = 2 (0000 0010)
#<<	Bitwise         |            left     |   shift	x << 2 = 40 (0010 1000)

#comparison operator
#     ==	Equal	x == y	
#     !=	Not equal	x != y	
#     >	    Greater than	x > y	
#     <	    Less than	x < y	
#     >=	Greater than or equal to	x >= y	
#     <=	Less than or equal to	x <= y

#logical operator
a = 900
b =231
print('logical operator')
print( a and b)
if (a and b < 100):
    print("hello")
else:
    print("mello")
if a or b <100:
    print("hello")
else:
    print("mello")
if not(a and b<100):
    print("help")
else:
    print("melp")

#identity operator
print('identity operator')
x = y =50
if x is not y:
    print("hello")
else:
    print("melo")
#membership operator
y = "is"
x = "shubham is good "
if x in y:
    print(x)
else:
    print(y)
#bitwise operator

#         Python Bitwise Operators
#         Bitwise operators are used to compare (binary) numbers:
#         
#         Operator       	Name	Description
#         & 	           AN       D	Sets each bit to 1 if both bits are 1
#         |	OR	           Se       ts each bit to 1 if one of two bits is 1
#          ^	           XO       R	Sets each bit to 1 if only one of two bits is 1
#         ~ 	           NO       T	Inverts all the bits
#         <<	           Ze       ro fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
#         >>	           Si       gned right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off