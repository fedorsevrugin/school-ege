for a in range(64):
    b = True
    for x in range(1000):
        if not((x & 29 != 0) <= ((x & 17 == 0) <= (x & a != 0))):
            b = False
    if b == True:
        print(a)
        break