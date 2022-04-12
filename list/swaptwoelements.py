#Python program to swap two elements in a list
#
#Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
#Output : [19, 65, 23, 90]
#
#Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
#Output : [1, 5, 3, 4, 2]

pos1 = int(input("enter the number"))
pos2 = int(input("enter the number"))
List = [23, 65, 19, 90]
size = len(List)
def swaping(List,pos1,pos2):
    temp = List[pos1]
    List[pos1] = List[pos2]
    List[pos2]=temp
    print(List)
print(swaping(List,pos1,pos2))

#enter the number1
#enter the number2
#[23, 19, 65, 90]
#None

