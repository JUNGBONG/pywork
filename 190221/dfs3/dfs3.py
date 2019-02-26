import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    a = list(map(int,input().split()))
    b = [a]
    for i in range(1,len(a)):
        c = list(map(int, input().split()))
        b.append(c)
    print(b)