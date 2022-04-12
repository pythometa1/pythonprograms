#Given a list of numbers, the task is to write a Python program to find the second largest number in the given list.
#Input: list1 = [10, 20, 4]
#Output: 10
#
#Input: list2 = [70, 11, 20, 4, 100]
#Output: 70

list = [10, 20, 4]

min = list[0]
secondmax = 0
for i in list:
    if i > min:
        min = i     
print(min)
for i in list:
    if i > secondmax and i != min:
        secondmax = i
print(secondmax)