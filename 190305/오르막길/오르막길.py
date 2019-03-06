import sys
sys.stdin = open('input.txt','r')
T=int(input())
A = list(map(int,input().split()))
maxV = 0
s = 0
start = 0
A.append(0)
for i in range(T):
    if(s==0 and A[i]<A[i+1]):
        start = i
        s=1
    elif(s==1 and A[i]>=A[i+1]):
        if(maxV<A[i]-A[start]):
            maxV=A[i]-A[start]
        s=0
print(maxV)