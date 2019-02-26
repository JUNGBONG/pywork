import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    Matrix = [[0] * n for i in range(n)]
    for i in range(1,n+1):
        for j in range(1, n+1):


