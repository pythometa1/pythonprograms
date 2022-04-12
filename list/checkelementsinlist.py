#Check if element exists in list in Python
test_list = [ 1, 6, 3, 5, 3, 4 ]
number = int(input("enter number"))
def chec(test_list,number):
    for i in range(int(len(test_list))):
        if (i==number):
            print("element present")
        else:
            pass
          
    print("element not present")


print(chec(test_list,number))
