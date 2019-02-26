import sys
sys.stdin = open('input.txt','r')

#부분집합이 합이 0인 경우가 있으면 1, 없으면 0을 출력하는 프로그램
#공집합 제외
T = int(input())
for test_case in range(1, T + 1):
    b, c = map(int, input().split())


    A = [i for i in range(1,13)]
    N = 12
    B = []
    count = 0
    count2 = 0
    for i in range(2**N):
        s = 0

        # i를 비트 단위로 접근
        for j in range(N-1, -1, -1):
            if(i&(1<<j) != 0): # A[j]가 포함되면
                s += A[j]
                B.append(A[j])
        if len(B) == b and s == c:
            count += 1

        elif i == 2**N-1:
            print(f'#{test_case} {count}')


        B=[]
