list1 = []
a = int(input('enter the number: '))
if a % 2 == 0:
    print(f'{a} is even')
else:
    for x in range(2,a):
        if a % x == 0:
            print(f'{a} is odd')
            break
    else:
        print(f'{a} is odd,beside {a} is a prime number')

b = input('enter the numbers:  Example : 88 99 22    ')
numbers = b.split(' ')
for hg in numbers:
    up = int(hg)
    list1.append(up)
print('even : ' , list(filter(lambda u:u % 2 == 0 , list1)))
print('odd : ' , list(filter(lambda y:y % 2 != 0 , list1)))