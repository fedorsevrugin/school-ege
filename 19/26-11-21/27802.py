def f(x,p):
    if x>=68 and p==2:
        return True
    elif x<68 and p==2:
        return False
    return f(x+1, p+1) or f(x+4, p+1) or f(x*5, p+1)


for x in range(1, 67):
    if f(x, 0):
        print(x)
        break