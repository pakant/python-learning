a = input('enter the txt: ')
b = a.split(' ')
s = 0
for c in b:
    d = list(c)
    if c.endswith('.') or c.endswith(',') or c.endswith('!') or c.endswith('?'):
        d.insert(-1,' ')
        b.insert(s,''.join(d))
        b.remove(c)
    s += 1
e = ' '.join(b)
f = e.split(' ')
while True:
    g = input('enter the words: ')
    if g == 'END':
        break
    f.remove(g)
print(*f,sep=' ')