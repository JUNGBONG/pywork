import sys
sys.stdin = open('input.txt','r')

T= int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    q = list(map(int,input().split()))
    for i in range(M):
        temp = q.pop(0)
        q.append(temp)
    print('#{0} {1}'.format(tc,q[0]))