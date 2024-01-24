# method 1 - using len function
str1 = "python"
print(len(str1))

# method 2 - using for loop
cnt = 0
for i in str1:
    cnt += 1
print(cnt)

# method 3 - using slicing
count = 0
while str1[count: ]:
    count += 1
print(count)

# method 4 - using lambda function
x = sum(map(lambda i : 1, str1))
print(x)

