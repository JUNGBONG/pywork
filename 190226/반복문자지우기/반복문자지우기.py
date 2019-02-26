import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range(1,T+1):
    word = input()
    stack=[]
    for i in range(len(word)):
        if len(stack) ==0:
            stack.append(word[i])
        elif stack[-1] != word[i]:
            stack.append(word[i])
            continue
        elif stack[-1] == word[i]:
            stack.pop()
    print(f'#{tc} {len(stack)}')