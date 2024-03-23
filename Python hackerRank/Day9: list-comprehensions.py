''' Problem Link : https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true '''

(x, y, z, n) = (int(input()), int(input()), int(input()), int(input()))

List = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
print(List)


''' OR
(x, y, z, n) = (int(input()), int(input()), int(input()), int(input()))

List = []

for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            if i+j+k != n:
                List.append([i, j, k])
                
print(List)  

'''
