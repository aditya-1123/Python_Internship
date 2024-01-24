# method 1
# using slicing
def reverse(str):
    print(str[ : :-1])

reverse("python")

# method 2
# using loop by getting first char and adding to front
s = "python"
str = ""
for i in s:
    str = i + str
print(str)

# method 3
# by traversing from back
s2 = "python"
i = len(s2)-1
while i>=0:
    print(s2[i], end="")
    i -= 1
