import sys
sys.stdin = open('input.txt','r')
T = int(input())


def bSearch(n, key):
    start = 1
    end = n
    cnt = 0
    while (start <= end):
        cnt += 1
        middle = int((start + end) // 2)
        if (middle == key):
            return cnt
        elif (middle > key):
            end = middle
        else:
            start = middle
    return 0
for tc in range(1, T + 1):


    a, b, c = map(int, input().split())
    A = bSearch(a, b)
    B = bSearch(a, c)

    if A==B:
        print(f'#{tc} 0')
    elif A<B:
        print(f'#{tc} A')
    elif A>B:
        print(f'#{tc} B')
