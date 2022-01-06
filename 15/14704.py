for a in range(50):
    b = True
    for x in range(100):
        for y in range(100):
            if not(((x < 6) <= (x * x < a)) and ((y * y <= a) <= (y <= 6))):
                b = False
    if b:
        print(a)