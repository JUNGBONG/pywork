import sys
sys.stdin = open('input.txt','r')
T=int(input())
a = list(map(int,input().split()))
stack = []
Hmax = 0
def f(T):
    global a,stack,Hmax
    cnt = 0
    for tc in range(T):
        cnt += 1
        if len(a)==1:
            return 0
        if (len(a)>=2 and len(stack)<=2):
            stack.append(a[tc])
            print(stack)
        if len(stack)==2:
            ro = stack.pop(0)
            hi = stack.pop(0)
            if hi-ro>0:
                if Hmax<hi-ro:
                    Hmax =hi-ro
            else:
                return 0
        if cnt==T-1:
            return Hmax
print(f(T))
