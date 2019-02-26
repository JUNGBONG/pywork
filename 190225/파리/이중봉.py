import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr=[list(map(int,input().split())) for i in range(N)]


    i=0
    j=0
    s=0
    max_v = 0
    while i<N-M+1:
        while j<N-M+1:
            s = 0
            for k in range(i,i+M):
                for l in range(j,j+M):
                    s += arr[k][l]
            if max_v < s:
                max_v = s

            j +=1
        j=0
        i +=1
    print(max_v)