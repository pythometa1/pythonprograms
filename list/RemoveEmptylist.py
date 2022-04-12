#Python – Remove empty List from List

test_list = [5, 6, [], 3, [], [], 9]
temp =[]
for i in test_list:
    if i != []:
        temp.append(i)
print(temp)
