a = 'hi ali and reza what are you doing? reza are you okay reza reza reza reza you you'
words = a.split(' ')
print(words)
list1 = []
for x in words:
    u = 0
    if len(list(filter(lambda i:i[0]==x,list1)))==0:
        for o in words:
            if x == o:
                u += 1
        list1.append((x , u))
print(list1)
list2 = sorted(list1, key=lambda tup: -1*tup[1])
print(list2)
list3 = list2[0:10]
print(list3)