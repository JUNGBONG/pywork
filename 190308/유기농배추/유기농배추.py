import sys
sys.stdin = open('input.txt','r')
def search(i,j,n,m):
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    q = []
    q.append(i)
    q.append(j)
    visited[i][j] = 1
    while(len(q) !=0): # 큐가 비어있지  않으면
        i = q.pop(0)
        j = q.pop(0)
        # arr[i][j] =0 #visited를 사용하지 않고 배추를 지우는 경우
        for k in range(4):
            ni = i +di[k]
            nj = j +dj[k]
            if(ni>=0 and ni<n and nj>=0 and nj<m):
                if(arr[ni][nj] == 1 and visited[ni][nj]==0): #지우는 경우if(arr[ni][nj] == 1):
                    q.append(ni)
                    q.append(nj)
                    visited[ni][nj] =1



T= int(input())
for tc in range(1,T+1):
    M,N,K = map(int,input().split())
    arr = [[0]*M for i in range(N)]
    visited=[[0]*M for i in range(N)]
    cnt=0
    for i in range(K):
        c, r = map(int,input().split())
        arr[r][c] = 1
    for i in range(N):
        for j in range(M):
            if(arr[i][j] == 1 and visited[i][j]==0):
                cnt+=1
                search(i,j,N,M)
    print(cnt)