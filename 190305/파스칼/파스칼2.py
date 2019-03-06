import sys
sys.stdin = open('input.txt','r')

T=int(input())
print('#{}'format(tc))
for tc in range(1,T+1):
    N = int(input())
    a = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i==j:
                a[i][0] = 1
                a[i][j] = 1
            elif i>j:
                a[i][j] =a[i-1][j-1] +a[i-1][j]


