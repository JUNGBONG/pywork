import sys
sys.stdin = open('input.txt','r')
T= int(input())
def npk(n,k):
    if (n==k):
        print(p)
    else:
        for i in range(k):
            if (used[i] == 0): # i가 사용전이면
                used[i] = 1 #사용한 숫자로 표시
                p[n] = a[i]
                npk(n+1,k)
                used[i] = 0 #다른 자리에서 사용 가능

for tc in range(1,T+1):
    N= int(input())
    arr = [list(map(int,input().split()))for i in range(N)]
    print(arr)




a=[1,2,3,4,5]
K = len(a)
p=[0]*K
used = [0]*K
npk(0,K)