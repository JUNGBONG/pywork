#카운트 배열
#0~9까지의 정수
# 4 5 6 7 8 9
a = list(map(int, input().split()))
b = int(input())
#카운트는 인덱스 백만까지일때 주로 사용
cnt = [0]*10 #0~9의 개수 저장

for i in range(6):
    cnt[a[i]] += 1

print(cnt)
print(b)