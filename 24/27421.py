f = open("27421.txt", "r")
mas = list(f.read())

maxim = 0
n = 0
for i in range(len(mas) - 1):
    if mas[i] != mas[i + 1]:
        n += 1
        if n > maxim:
            maxim = n
    else:
        n = 1

print(maxim) #35
