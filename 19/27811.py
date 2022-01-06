def f(x,p):
    if x>=48 and p==2:
        return True
    elif x<48 and p==2:
        return False
    return f(x+1, p+1) or f(x+4, p+1) or f(x*2, p+1)


for x in range(1, 48):
    if f(x, 0):
        print(x)
        break