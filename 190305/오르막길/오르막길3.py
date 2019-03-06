import sys
sys.stdin = open('input.txt','r')
N= int(input())
h= list(map(int,input().split()))+[0]
start = 0 #오르막 구간의 시작 인덱스
status = 0 #오르막 구간1, 나머지 0 (오르막길이의 상태를 나타냄)
maxV=0
for i in range(N): #오른쪽과 비교할 자리i
    if(status==0 and h[i]<h[i+1]):
        start = i
        status = 1
    elif(status ==1 and h[i]>=h[i+1]): #i에서 오르막이 끝나면
        diff = h[i] - h[start] # 오르막 구간의 높이차
        if(maxV<diff): # 가장 큰 오르막 찾기
            maxV=diff
        status = 0
print(maxV)
