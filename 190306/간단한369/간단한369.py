import sys
sys.stdin = open('input.txt','r')
N = int(input())
a=['3','6','9']
i=1
result=[]
cnt=0
while True:
    for j in str(i):
        if j in a:
            cnt+=1
    if i != 1 :
        print(" "+'-'*cnt,end='')

    if cnt==0:
        print(i,end='')

    cnt=0

    i += 1
    if i==N+1:
        break