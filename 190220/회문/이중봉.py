import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    word = input()
    for i in range(len(word)//2):
        result = 1
        if word[i]==word[len(word)-1-i]:
            continue
        else:
            result = 0

    print(f'#{tc} {result}')
