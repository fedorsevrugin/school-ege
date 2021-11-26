def f(x,p):
    if x>=48 and p==3:
        return True
    elif (x<48 and p==3) or x>=48:
        return False
    elif p%2==0:
        return f(x+1, p+1) or f(x+4, p+1) or f(x*2, p+1)
    else:
        return f(x+1, p+1) and f(x+4, p+1) and f(x*2, p+1)


for x in range(1, 48):
    if f(x, 0):
        print(x)