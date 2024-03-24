''' Problem Link : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true   '''

(n, arr) = (int(input()), map(int, input().split()))
    
list1 = sorted(set(arr))
print(list1[-2])

 ''' OR 
list1 = []
cnt = 0
set1 = set(arr)
for i in set1:
    cnt += 1
    list1.append(i)
    
list1.sort()
print(list1[cnt-2])

'''
