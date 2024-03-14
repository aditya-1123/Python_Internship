''' Problem Link : https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true   '''

n=int(input())
if(n<0):
    n=-n

for i in range(0,n):
    i=i**2
    print(i)

# OR print([i**2 for i in range(n)])
