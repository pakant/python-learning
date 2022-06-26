take_numbers = input('enter the number:   (Example : 10-2) ').split('-')
(a,b) = map(lambda x:int(x),take_numbers)
def plus ():
    print(f'{a} + {b}  :  {a + b}')
def minus ():
    print(f'{a} - {b}  :  {a - b}')
def divided ():
    print(f'{a} / {b}  :  {a / b}')
def times ():
    print(f'{a} * {b}  :  {a * b}')
plus()
minus()
divided()
times()