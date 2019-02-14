import sys
sys.stdin = open('input.txt','r')

for tc in range(1,11):
    view=0
    N = int(input())
    b = list(map(int, input().split()))
    for i in range(2,len(b)-2):
        short=256
        if b[i]>b[i+1] and b[i]>b[i+2] and b[i]>b[i-1] and b[i]>b[i-2]:
            c = [b[i]-b[i+1],b[i]-b[i+2],b[i]-b[i-1],b[i]-b[i-2]]
            for j in c:
                if short > j:
                    short = j
            view += short








    print('#{} {}'.format(tc,view))