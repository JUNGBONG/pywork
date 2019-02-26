def find(x):
    r= 99
    c = x
    while(r<0):
        while(r>0 and ladder[r][c-1] ==0 and ladder[r][c+1]):
            r -= 1
        dc=1
        if(r>0 and ladder[r][c-1] == 1):
            dc = -1
        else:
            dc = 1
        while(ladder[r][c+dc])