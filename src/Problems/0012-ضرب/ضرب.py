a = input('enter the number: ')
b = input('enter the number: ')
list1 = []
c = list(a)
d = list(b)
f = 0
for x in range(len(c)-1,-1,-1):
    y = c[x] + f * '0'
    f += 1
    g = 0
    for o in range(len(d)-1,-1,-1):
        h = d[o] + g * '0'
        list1.append(int(y) * int(h))
        g += 1
for t in range(0,len(list1)-1):
    list1.append(list1[t] + list1[t + 1])
    list1.pop(1)
print(list1[-1])