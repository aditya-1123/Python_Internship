# Problem link : https://www.hackerrank.com/challenges/py-if-else/submissions/code/294097963

n = int(input())
if(n%2==1):
    print("Weird")
elif(n%2==0):
    if(n>2 and n<=5): 
        print("Not Weird")
    elif(n>6 and n<=20):
        print("Weird")
    elif(n>20):
        print("Not Weird")
