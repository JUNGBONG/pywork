import sys
sys.stdin = open('input.txt','r')
T = int(input())


def Aton(inputlist):
    alist = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    result = []
    for j in inputlist:
        for i, v in enumerate(alist):
            if j == v:
                result.append(i)
    return result

def NtoA(inputlist):
    alist = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    result = []
    for j in inputlist:
        for i, v in enumerate(alist):
            if j == i:
                result.append(alist[i])
    return result

for tc in range(1,T+1):
    n = list(input().split())[1]


    a = list(input().split())
    a = sorted(Aton(a))
    b = NtoA(a)
    print(f'#{tc}')
    for i in b:
        print(i, end=" ")