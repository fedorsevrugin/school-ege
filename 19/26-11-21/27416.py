def f(k, s, p):
    if s+k>=77 and p==2:
        return True
    elif s+k<77 and p==2:
        return False
    return f(k, s+1, p+1) or f(k, s+4, p+1) or f(k, s*2, p+1) or f(k+1, s, p+1) or f(k+4, s, p+1) or f(k*2, s, p+1)

k=7
for s in range(1, 69):
    if f(k, s, 0):
        print(s)
        break