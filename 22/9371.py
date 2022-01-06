for x in range(100, 1000):
    L = x
    M = 65
    k = x
    if L % 2 == 0:
        M = 52
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    if M == 26:
        print(k) # 130