a = int(input('enter the number: '))
list = []
b = 0
l = 0
while True:
    if l == 0:
        b += 1
        print(b)
    if l == 1:
        b += 1
        print(b)
        list.append(b)
    if l != 0 or 1:
        for x in list:
            b += x
            list.pop(0)
        list.append(b)
        if b < a:
            print(b)
    l += 1
    if b >  a:
        break