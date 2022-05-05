list1 = []
def name():
    while True:
        a = input('enter the name :')
        if a=='END':
            print(list1)
            break
        line = a.split(' ')
        for x in line:
            list1.append(x)
name()
def number():
    b= int(input('enter the number: '))
    result=(list(filter(lambda i:len(i)<b,list1)))
    print(list(map(lambda u:f'Hello {u}',result)))
    print(result)
number()