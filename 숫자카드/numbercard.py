import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    result=0
    N=int(input())
    A=list(map(int,input()))
    counts=[0]*10
    B=[0]*len(A)
    maxcard=0
    maxcardnum=0
    for i in A:
        counts[i] += 1
    for i2 in range(0,len(counts)):
        if maxcard < counts[i2]:
            maxcard = counts[i2]
    print(counts)

    for j in range(1,len(counts)):
        counts[j] = counts[j-1]+counts[j]
    for k in range(len(B)-1,-1,-1):
        counts[A[k]] -= 1
        B[counts[A[k]]]=A[k]


    print(counts)
    maxcardnum = counts[len(counts)-1]
    print(maxcardnum)

    print(f'#{maxcardnum} {maxcard}')