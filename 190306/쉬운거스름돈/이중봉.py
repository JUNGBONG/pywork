def f(n, c):
    global N
    if c == 8:
        return 1
    else:
        if N // a[c] > 0:
            b[c] = N // a[c]
            N = N - N // a[c] * a[c]
            f(n, c + 1)
        else:
            f(n, c + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    a = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    b = [0] * 8
    f(N, 0)
    print(f'#{tc}')
    for i in b:
        print(i, end=" ")
    print()
