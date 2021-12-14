for a in range(10000):
    b = True
    for x in range(11):
        for y in range(11):
            if not(((x <= 9) <= (x * x <= a)) and ((y * y <= a) <= (y <= 9))):
                b = False
    if b:
        print(a) # 99