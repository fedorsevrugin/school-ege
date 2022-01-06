f = list(open("29672.txt", "r"))

n = 0
for i in f:
    if i.count("E") > i.count("A"):
        n += 1

print(n) #467
