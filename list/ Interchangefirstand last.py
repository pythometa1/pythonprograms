 #1: Find the length of the list and simply swap the first element with (n-1)th element.
#Input : [12, 35, 9, 56, 24]
#Output : [24, 35, 9, 56, 12]
#
#Input : [1, 2, 3]
#Output : [3, 2, 1]

l1 = [12, 35, 9, 56, 24]
size = len(l1)
temp = []
temp =l1[0]
l1[0]=l1[size-1]
l1[size-1]=temp
print(l1)
