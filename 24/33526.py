f = open("33526.txt", "r")

a = list(f.read())
b = []
for i in range(len(a) - 2):
    if a[i] == a[i + 2]:
        b.append(a[i + 1])

alf = "ABCDEFGHIJKLMNOP"
maxim = 0
for i in alf:
    if b.count(i) > maxim:
        maxim = b.count(i)
        k = i

print(k) #D
