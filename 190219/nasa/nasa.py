import sys
sys.stdin = open('input.txt','r')
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    c = []
    for i in range(len(a)):
        if i%2==0:
            b.append(a[i])
        else:
            c.append(a[i])
    d = list(set(b) - set(c))
    e = list(set(c) - set(b))
    f = b.index(d[0])
    g = c.index(e[0])
    b[0],b[f] = b[f],b[0]
    c[0],c[f] = c[f],c[0]
    b[-1], b[g] = b[g], b[-1]
    c[-1], c[g] = c[g], c[-1]
    for i in range(n-1):
        if c[i] != b[i+1]:
            indexnum = b.index(c[i])
            b[indexnum],b[i+1] = b[i+1], b[indexnum]
            c[indexnum], c[i + 1] = c[i + 1], c[indexnum]


    print(b)
    print(c)
    # for i in range(len(a)):
    #     for j in range(len(b)):
    #         if b[i] == c[j]:
