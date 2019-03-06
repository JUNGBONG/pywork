import sys
sys.stdin = open('input.txt','r')
T= int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split())) for i in range(N)]
    cnt = 1
    cnt2 = 1
    wordcnt = 0
    for i in range(N-1):
        for j in range(N-1):
            if (arr[i][j] == 1 and arr[i][j+1] == 1):
                cnt += 1

            else:
                if cnt == M:
                    wordcnt += 1
                cnt = 1

            if (arr[j][i] == 1 and arr[j+1][i] == 1):
                cnt2 += 1

            else:
                if cnt2 == M:
                    wordcnt += 1
                cnt2 = 1

        if cnt == M:
            wordcnt += 1
            cnt = 1
        if cnt2 == M:
            wordcnt+=1
            cnt2= 1
        cnt = 1
        cnt2 = 1
    print(wordcnt)


