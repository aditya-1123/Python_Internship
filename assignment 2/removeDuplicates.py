
list1 = [1, 1, 2, 7, 3, 6, 7, 9, 3, 3, 8, 6]

# method 1 By converting list to set
res = set(list1)
print(list(res))

# method 2 Using for loop
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)


