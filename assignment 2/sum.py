
# method 1 Using for loop & range function
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum1 = 0
for i in range(len(list1)):
    sum1 += list1[i]
print(sum1)

# method 2 Using simple for loop
ans = 0
for i in list1:
    ans += i
print(ans)

# method 3 Using lambda reduce function
from functools import reduce
sum2 = reduce(lambda x,y : x+y, list1)
print(sum2)

# method 4 Using Sum function
total = sum(list1)
print(total)

# method 5 using while loop
res = 0
i=0
while i < len(list1):
    res += list1[i]
    i += 1

print(res)





