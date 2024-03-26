''' Problem Link : https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true  '''

marks = student_marks[query_name]

sum = 0
for i in marks:
    sum += i
    
res = sum/len(marks)
print("{:.2f}".format(res))

''' OR

print(f"{sum(student_marks[query_name]) / 3:.2f}")

'''
