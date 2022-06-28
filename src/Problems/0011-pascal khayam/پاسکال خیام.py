a = [1,1]
o = int(input('enter the number: '))
def next(p):
    list1 = []
    for x in range(0,len(p)-1):
        list1.append(p[x] + p[x + 1])
    list1.insert(0,1)
    list1.insert(len(list1),1)
    return list1
print(o * ' ','1')
print((o - 1)*' ',*a,sep=' ')
for r in range(2,o + 1):
    a = next(a)
    print((o - r)*' ',*a,sep=' ')