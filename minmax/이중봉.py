T = int(input())
for tc in range(1,T+1):
    result=0
    N=int(input())
    A=list(map(int,input().split()))
    for i in range(0,len(A)-1):
        for j in range(i+1,len(A)):
            if A[i]<A[j]:
                A[i],A[j]=A[j],A[i]
    result=A[0]-A[len(A)-1]

    print(f'#{tc} {result}')