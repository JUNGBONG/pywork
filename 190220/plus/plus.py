import sys
sys.stdin = open('input.txt','r')
T= int(input())
for tc in range(1,T+1):
    A = list(map(int,input().split()))
    h1,m1,h2,m2 = A[0],A[1],A[2],A[3]
    ht , mt =0,0
    if m1+m2//60 > 1:
        ht += (m1+m2)//60
        mt = (m1+m2)%60
    else:
        mt = (m1+m2)%60
    ht+= (h1+h2)%12
    print(f'#{tc} {ht} {mt}')