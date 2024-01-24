
list1 = [12, 45, 76, 10, 23, 89, 33, 80]

# method 1 Using max() function
print(f"min is : {min(list1)}")

# method 2 Using for loop
smallest = list1[0]
for no in list1:
    if no < smallest:
        smallest = no
print(f"min is : {smallest}")