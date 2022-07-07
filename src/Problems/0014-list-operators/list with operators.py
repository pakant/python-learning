a = input('enter the numbers: ')
list1 = []
e = a.split(' ')
b= list(map(lambda c:int(c),e))
d = sorted(b)
print('Max is',d[-1])
print('Min is',d[0])
f = d[0] + d[1]
y = d[0] * d[1]
for x in range(2,len(d)):
    f += d[x]
    y *= d[x]
print('Avg is',f/(len(d)))
if len(b) % 2 != 0:
    print('Mean is',d[int(len(d)/2)])
else:
    print('Mean is',(b[int(len(b)/2)-1]+b[int(-1*(len(b)/2))]) / 2)
print(f'Last 3 numbers are,{b[-3],b[-2],b[-1]}')
for g in b:
    i = 0
    for h in b:
        if g == h:
            i += 1
    list1.append((g,i))
sorts = sorted(list1 ,key=lambda tup: -1*tup[1])
o = 0
while o < (len(sorts)):
    if sorts[o][1] > 1:
        for r in range(0,sorts[o][1]-2):
            sorts.remove(sorts[r])
    o += 1
print(f'Two numbers with highest count aresorts,{sorts[0][0]} and {sorts[1][0]}')
print('Sum of all is',f)
print('Product of all is',y)