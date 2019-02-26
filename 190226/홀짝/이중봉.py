import sys
sys.stdin = open('input.txt','r')
T= int(input())
for tc in range(1,T+1):
    number =int(input())
    if number%2 ==0:
        result='Even'
    else:
        result='Odd'
    print(f'#{tc} {result}')