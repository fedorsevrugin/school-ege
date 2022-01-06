file = open("37336.txt", "r")
mas = list(file)
file.close()
mas = [int(i) for i in mas]

maxsum = -10000
k = 0
for i in range(len(mas) - 1):
    if (mas[i] % 3 == 0) or (mas[i + 1] % 3 == 0):
        k += 1
        if mas[i] + mas[i + 1] > maxsum:
            maxsum = mas[i] + mas[i + 1]

print(k, maxsum) #2802 1990
