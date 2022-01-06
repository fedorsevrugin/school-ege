for a in range(10000):
    b = True
    for x in range(100):
        for y in range(100):
            if not((3*x +7*y < a) or (x >= y) or (y > 6)):
                b = False
    if b:
        print(a)
        break