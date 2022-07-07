a = int(input('enter the even number and biger than number 2: '))
def prime_number(b):
    i = 1
    while i < b:
        i += 1
        if b % i == 0:
            return b == i
for x in range(2,a + 1):
    if prime_number(x):
        if prime_number(a-x):
            print(x,a-x)