import sys
sys.stdin = open('input.txt','r')
# NxN 배열 입력
N=int(input())
arr= [list(map(int,input().split())) for i in range(N)]
# 0으로 초기화된 5x5 배열 만들기
b= [[0]%5 for i in range(5)]
print(b)
b[2]b[2] = 30
print(arr)
print(arr[1])
print(arr[2][2])