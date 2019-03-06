import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    P, Q, R, S, W = map(int,input().split())
    r1 = P*W
    if (W-R) <= 0:
        r2 = R*Q
    else:
        r2 = (W-R)*S + R*Q
    if r1<=r2:
        final = r1
    else:
        final = r2
    print(final)