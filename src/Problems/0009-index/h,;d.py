list = []
list1 = []
while True:
    b = input()
    if b == 'END':
        break
    line = b.split('.')
    for i in line:
        list.append(i)
while True:
    a = input()
    if a == 'END':
        break
    list1.append(a)
for x in list1:
    for o in list:
        if x in o:
            print(o)
            if x.casefold() == o.casefold():
                print(o)