import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    D, A, B, F = map(int,input().split())
    result = F*(D/(A+B))

    print(f'#{tc} {result}')