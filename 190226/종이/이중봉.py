import sys
sys.stdin = open('input.txt','r')

T=int(input())
for tc in range(1,T+1):
    N= int(int(input())/10)
    f=[0]*(N+1)
    f[0] = 1
    f[1] = 1
    f[2] = 3
    for i in range(3,N+1):
        f[i] += f[i-1] +2*f[i-2]
    print(f'#{tc} {f[N]}')