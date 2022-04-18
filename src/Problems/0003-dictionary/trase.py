a = "4 63 1000 464 20"
b = a.split()
print(b)
list2= []
c= list(map(lambda x: int(x) + 1,b))
print(c)
for up in b:
    list2.append(int(up))
print(list2)

lambda x: int(x) + 1
y= int(x) + 1