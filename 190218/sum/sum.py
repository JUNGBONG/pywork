import sys
sys.stdin = open('input.txt','r')
for tc in range(0,10):
    tn = int(input())
    a = [list(map(int,input().split())) for i in range(0,100)]
    print(a)
    maxv = 0
    maxv2 = 0
    maxvt = 0
    newv1 = 0
    newv2 = 0
    for i in range(len(a)):
        for j in range(len(a)):
            newv1 += a[i][j]
            newv2 += a[j][i]


        maxv = newv1
        maxv2 = newv2
        if maxvt<maxv or maxvt<maxv2
            if maxv>maxv2:
                maxvt = maxv
            else:
                maxvt = maxv2
        newv1 = 0
        newv2 = 0

