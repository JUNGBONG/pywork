import sys
sys.stdin = open('input.txt','r')
T=int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for i in range(N)]
    i=0
    speed=0
    distance=0
    while True:
        if len(arr[i])==1:
            distance += speed
        else:
            if arr[i][0] == 1:
                speed += arr[i][1]
                distance += speed
            if arr[i][0] == 2:
                speed -= arr[i][1]
                if speed >= 0:
                    distance += speed

                else:
                    speed=0
        i+=1
        if i == (len(arr)):
            break
    print(f'#{tc} {distance}')
