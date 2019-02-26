import sys
sys.stdin = open('input.txt','r')

for tc in range(1,11):
    N= int(input())
    arr = [list(map(int,input().split())) for i in range(N)]
    stack = 0
    i=0
    j=0
    while i<N:
        while j<N:
            if arr[j][i] == 1:
                for k in range(j,N):
                    if arr[k][i] ==2:
                        j = k
                        stack +=1
                        break

            j += 1
        i += 1
        j=0

    print(f'#{tc} {stack}')

