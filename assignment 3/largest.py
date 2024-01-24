
list1 = [12, 45, 76, 23, 89, 33, 80]

# method 1 Using max() function
print(f"max is : {max(list1)}")

# method 2 Using for loop
largest = 0
for no in list1:
    if no > largest:
        largest = no
print(f"max is : {largest}")

