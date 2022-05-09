def getNames():
    list1 = []
    while True:
        a = input('enter the name :')
        if a=='END':
            break
        line = a.split(',')
        for x in line:
            list1.append(x)
    return list1
l2 = getNames()
print(l2)
def greet(list2):
    b= int(input('enter the number: '))
    result=(list(filter(lambda i:len(i)<b,list2)))
    return result
l3 = greet(l2)
def hello(result1):
    jack = list(map(lambda u:f'Hello {u}',result1))
    print(jack)
    return jack
l4 = hello(l3)
def membersoflist(list4):
    print(list4)
membersoflist(l3)