import sys
sys.stdin = open('input.txt','r')
N =int(input())
arr = [list(map(int,input().split())) for i in range(N)]


b= [[0]*5 for i in range(5)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

sum=0

for i in range(N):
    for j in range(N): #  배열 A의 모든 원소에 대해
        print(i, j, end=' ')
        print()
        for k in range(4): # k번 방향 탐색
            ni = i + di[k]
            nj = j + dj[k]
            if(ni>=0 and ni<N and nj>=0 and nj<N): # 배열을 벗어나지 않는 경우
                sum += abs(arr[ni][nj]-arr[i][j])
                print(sum)