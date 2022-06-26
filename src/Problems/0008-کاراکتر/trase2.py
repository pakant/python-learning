o = int(input('enter the number: '))
a = [1,1]
def next(i):
    list1 = []
    n = 1
    for x in i:
        list1.append(x + i[n])
        if i[n] == 1:
            break
        n += 1
    list1.insert(0,1)
    list1.insert(len(i),1)
    return list1
for b in range(1,o + 1):
    if b == 1:
        print(o * ' '+' 1')
        print((o - 1) * ' ','1 1')
    if b != 1:
        a = next(a)
        print((o - b)* ' ',*a,sep=' ')