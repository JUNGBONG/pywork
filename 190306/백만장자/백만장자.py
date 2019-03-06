import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    N=int(input())
    a = list(map(int,input().split()))

    b = [0]*N
    sV= a[-1]
    sumprice=0
    for i in range(len(a)-1,-1,-1):
        if a[i-1] <= sV:
            b[i] = sV

        else:
            b[i] = sV
            sV = a[i-1]
        sumprice += (b[i] - a[i])
    print(sumprice)
