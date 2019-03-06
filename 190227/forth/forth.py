import sys
sys.stdin = open('input.txt','r')
T= int(input())
for tc in range(1,T+1):
    Forth =list(input().split())
    a=[]
    result=""
    for i in Forth:
        if i != '+' and i != '-' and i != '*' and i != '/':
            a.append(i)
        elif i =='.':
            result = Forth.pop()
            if len(Forth) >=2:
        else:
            if len(Forth) >2:
                op2 = Forth.pop()
                op1 = Forth.pop()
                if op1 != '+' and op1 != '-' and op1 != '*' and op1 != '/' and op2 != '+' and op2 != '-' and op2 != '*' and op2 != '/':
                    if i =="+":
                        temp = (int(op1) + int(op2))
                        Forth.append(temp)
                    elif i =="-":
                        temp = (int(op1) - int(op2))
                        Forth.append(temp)
                    elif i =="*":
                        temp = (int(op1) * int(op2))
                        Forth.append(temp)
                    elif i =="/":
                        temp = (int(op1) / int(op2))
                        Forth.append(temp)
                else:
                    continue
            else:
                result ='Error'
                break
    print(result)