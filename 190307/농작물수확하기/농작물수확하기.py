import sys
sys.stdin = open('input.txt','r')
T= int(input())
def bfs(n,cntnumbersum):

    s=arr[n//2][n//2]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    q = [0]*n*n*2
    front = -1
    rear = -1
    visited = [[0]*n for i in range(n)]
    #시작점 추가
    rear += 1
    q[rear] = n//2
    rear += 1
    q[rear] = n//2
    visited[n//2][n//2] = 1
    cnt=1
    while(front != rear):
        front += 1
        i = q[front]
        front += 1
        j = q[front]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if(ni>=0 and ni<n and nj>=0 and nj<n):
                if(visited[ni][nj] == 0):
                    # print(ni,nj)
                    rear += 1
                    q[rear] = ni
                    rear += 1
                    q[rear] = nj
                    visited[ni][nj] = visited[i][j] + 1
                    s += arr[ni][nj]
                    cnt +=1
        if cnt==cntnumbersum:
            return s
    return s

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for i in range(N)]

    cntnumber =[1]
    num2=1
    cntnumbersum=0
    for i in range(1,N):
        b = (num2*2+2)
        num2 = num2+2
        cntnumber.append(b)

    for i in range(1,N):
        print(cntnumbersum)
        cntnumbersum += cntnumber[i]
    print('#{} {}'.format(tc,bfs(N,cntnumbersum)))
    print(cntnumbersum,len(cntnumber), cntnumber)
