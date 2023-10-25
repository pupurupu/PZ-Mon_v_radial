#a = [44, 55, 12, 42, 94, 18, 6, 67]
a = [99, 33, 12, 22, 7]
#a = input("-> ").split()
b = []
c = []
x = 0
z = 0
for i in range(len(a)):
    a[i]=int(a[i])
while len(a) != 0:
    for i in range(len(a) - 1):
        if a[i] >= a[i + 1]:
            x = a[i]
            a[i] = a[i + 1]
            a[i + 1] = x
    for i in reversed(range(len(a) - 1)):
        if a[i] >= a[i + 1]:
            x = a[i]
            a[i] = a[i + 1]
            a[i + 1] = x
    b.append(a[0])
    del a[0]
    if len(a) !=0:
        c.insert(0, a[len(a) - 1])
        del a[len(a) - 1]
s = b+c
print(s)
