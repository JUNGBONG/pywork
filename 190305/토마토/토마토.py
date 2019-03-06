import sys
sys.stdin = open('input.txt','r')
M,N = map(int,input().split())
a = [list(map(int,input().split())) for i in range(N)]

def bfs(i,j,n,m):
    global cnt2
    global q
    cnt=0
    di =[0, 1, 0, -1]
    dj =[1, 0, -1, 0]

    visited = [[0]*m for i in range(n)]
    for i in range()
    q.append(i) #시작점 인큐
    q.append(j)
    visited[i][j] = 1
    while(len(q) !=0):
        i=q.pop(0) #디큐
        j=q.pop(0)
        for k in range(4):  # 인접한 4방향에 대해
            ni = i + di[k]
            nj = j + dj[k]
            if (ni >= 0 and ni < n and nj >= 0 and nj < m and a[ni][nj]!=-1):
                if (a[ni][nj] != 1 and visited[ni][nj] == 0):
                    q.append(ni)
                    q.append(nj)
                    visited[ni][nj] = visited[i][j] + 1
                    if visited[ni][nj] != cnt2:
                        cnt2 +=1
            elif (ni >= 0 and ni < n and nj >= 0 and nj < m and a[ni][nj]==-1):
                visited[ni][nj] = -1
        cnt = 0
    print(visited)
    for i in range(n):
        for j in range(m):
            if visited[i][j]==0:
                return -1
    return visited
cnt2=0
q = []
for i in range(N):
    for j in range(M):
        if a[i][j] ==1:
            q.append(i)
            q.append(j)
print(len(q))