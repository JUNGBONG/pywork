def mycopy1(n,k):
    if n==k:
        return
    else:
        B[n] = A[n]
        return mycopy1(n+1,k)
A = [1,2,3]
B = mycopy1(A[0],len(A))

