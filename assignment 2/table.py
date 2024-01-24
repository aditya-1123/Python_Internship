#method 1

print("Table of 7")
for i in range(1,11):
    print(f"7 * {i} = {7*i}")

#method 2
print("\nUsing lambda function")
nos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = list(map(lambda i : 7*i, nos))
print(x)
