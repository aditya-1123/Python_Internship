#method1

print("Cube of nos from 1 to 10")
for i in range(1,11):
    print(f"{i} : {i**3}")

#method2

print("\nUsing while loop")
i=1
while i<11:
    print(f"{i} : {i**3}")
    i += 1
