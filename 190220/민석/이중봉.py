import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    b = list(map(int,input().split()))
    allstudent = list(range(1, N+1))
    result = []
    for i in allstudent:
        if i not in b:
            result.append(i)
    print(f'#{tc}', end=" ")
    for j in result:
        print(j, end=" ")
    print()

