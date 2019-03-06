import sys
sys.stdin = open('input.txt','r')
T= int(input())
def f(i,j,n,c):
    global cnt
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    if (maze[i][j] == 3):
        if cnt > c:
            cnt =c
        return
    else:
        maze[i][j] = 1 #방문한 칸으로 미로에 직접 표시
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if(ni>=0 and ni<n and nj>=0 and nj<n):
                if(maze[ni][nj] !=1):
                    f(ni,nj,n,c+1)
        maze[i][j] = 0
        return

for tc in range(1,T+1):
    N=int(input())
    maze = [list(map(int,input())) for i in range(N)]
    startI = -1
    startJ = -1
    cnt = 100000
    for i in range(N):
        for j in range(N):
            if(maze[i][j]==2):
                startI = i
                startJ = j
                break
        if(startI!=-1):
            break
    f(startI, startJ, N, 0)
    if cnt==100000:
        cnt=0
    else:
        cnt-=1
    print('#{0} {1}'.format(tc,cnt))