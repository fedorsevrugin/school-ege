def f(x, p):
    if x>=48 and (p==4 or p==2):
        return True
    elif (x<48 and p==4) or x>=48:
        return False
    elif p%2==1:
        return f(x+1, p+1) or f(x+4, p+1) or f(x*2, p+1)
    else:
        return f(x+1, p+1) and f(x+4, p+1) and f(x*2, p+1)

def f1(x, p):
    if x>=48 and p==2:
        return True
    elif (x<48 and p==2) or x>=48:
        return False
    elif p%2==1:
        return f1(x+1, p+1) or f1(x+4, p+1) or f1(x*2, p+1)
    else:
        return f1(x+1, p+1) and f1(x+4, p+1) and f1(x*2, p+1)

def f2(x, p):
    if x>=48 and p==4:
        return True
    elif (x<48 and p==4) or x>=48:
        return False
    elif p%2==1:
        return f2(x+1, p+1) or f2(x+4, p+1) or f2(x*2, p+1)
    else:
        return f2(x+1, p+1) and f2(x+4, p+1) and f2(x*2, p+1)

for x in range(1, 48):
    if f(x, 0):
        print(x)

for x in range(1, 48):
    if f1(x, 0):
        print(x, " ", 1)

for x in range(1, 48):
    if f2(x, 0):
        print(x, " ", 2)