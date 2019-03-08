import sys
sys.stdin = open('input.txt','r')
def bfs(n,si,sj):
    cnt = 0
    di = [1,0,-1,0]
    dj = [0,1,0,-1]
    q = [0]*n*n*2

    visited[si][sj] = 1

    front = -1
    rear = -1

    rear += 1
    q[rear] = si
    rear += 1
    q[rear] = sj

    while(front!=rear):

        front += 1
        i = q[front]
        front += 1
        j = q[front]

        arr[i][j] = 0
        cnt+=1
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if(ni>=0 and ni<n and nj>=0 and nj<n):
                if(arr[ni][nj] >=1 and visited[ni][nj]==0):
                    rear += 1
                    q[rear] = ni
                    rear += 1
                    q[rear] = nj
                    arr[ni][nj] =0
    return cnt



N= int(input())
arr = [list(map(int,input())) for i in range(N)]
visited=[[0]*N for i in range(N)]
result=[]
cnt2=0
for i in range(N):
    for j in range(N):
        if arr[i][j] ==1:
            result.append(bfs(N,i,j))
            cnt2+=1
result.sort
print(cnt2)
for i in result:
    print(i)