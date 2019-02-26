def f(n,k):
    if(n==k):
        print(p)
    else:
        for i in range(1, k+1):
            p[n] = i
            f(n+1, k)



K = 5
p = [0]*K
f(0,K)