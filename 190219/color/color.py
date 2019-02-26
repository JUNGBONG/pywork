import sys
sys.stdin = open('input.txt','r')
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    b = []
    for i in range(N):
        a = list(map(int, input().split()))
        b.append(a)
    print(b)
