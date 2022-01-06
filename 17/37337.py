file = open("37337.txt", "r")
mas = list(file)
file.close()
mas = [int(i) for i in mas]

maxsum = -10000
k = 0
d = 160
p = 7

for i in range(len(mas) - 1):
    for j in range(i + 1, len(mas)):

        if ((mas[i] % d) != (mas[j] % d)) and ((mas[i] % p == 0) or (mas[j] % p == 0)):
            k += 1
            if mas[i] + mas[j] > maxsum:
                maxsum = mas[i] + mas[j]

print(k, maxsum) #12749665 19989
