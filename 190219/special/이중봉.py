import sys
sys.stdin = open('input.txt','r')
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        # 최소값 찾는 처리
        for k in range(i+1, len(arr)):
            if arr[k] < arr[min_index]:
                min_index = k
        # 최소값의 위치를 바꿔주는 처리
        tmp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = tmp
    return arr
for tc in range(1, T + 1):
    n = int(input())
    a = list(map(int, input().split()))
    b = selection_sort(a)
    c = []
    for i in range(len(b)):

        c.append(b[len(b)-1-i])
        c.append(b[i])
    d = c[0:10]
    print(f'#{tc}',end=' ')
    for j in d:
        print(j,end=' ')
    print()

