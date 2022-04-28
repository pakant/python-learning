from numpy import array
list2 = []
list1 = []
a = int(input())
b = int(input())
u = 0
while u < a:
    ab = input(f'enter {b} number: ')
    line1 = ab.split(' ')
    list1.append(list(map(lambda x: int(x),line1)))
    u += 1
hg = array(list1)
t = int(input())
nv = 0
while nv < b:
    mc= input(f'enter {t} number: ')
    line2=mc.split(' ')
    list2.append(list(map(lambda r: int(r),line2)))
    nv += 1
yt = array(list2)
print(hg.dot(yt))