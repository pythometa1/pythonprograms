#Python program to find smallest number in a list
#Input : list1 = [10, 20, 4]
#Output : 4
#
#Input : list2 = [20, 10, 20, 1, 100]
#Output : 1

list2 = [20, 10, 20, 1, 100]
min = list2[0]
for i in list2:
    if i<min:
        min = i
print(min)

min= list2[0]

for i in list2:
    if i>min:
        min=i
print(min)
        