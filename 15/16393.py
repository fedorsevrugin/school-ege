for a in range(10000):
    b = True
    for x in range(100):
        for y in range(100):
            if not((2*x + 3*y > 30) or (x + y <= a)):
                b = False
    if b:
        print(a)
        break