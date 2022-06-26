a = input('enter the numbers:  Example : 12 35 68  ')
numbers = a.split(' ')
list = []
for x in numbers:
    up = int(x)
    list.append(up)
print(sorted(list))