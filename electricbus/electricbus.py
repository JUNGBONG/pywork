import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    result=0
    K,N,M=map(int,input().split())
    B=list(map(int,input().split()))
    A=[0]*N
    for i in B:
        A[i] = K
    jump=K
    Fuel=K
    station=0

    for j in range(1,len(A)):
        Fuel -=1
        if Fuel == 0:
            if A[j] == K:
                Fuel = K
            else:
                for i in range(1,K):
                    if A[j-i]==K:








    print(f'#{tc} {result}')
