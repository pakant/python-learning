a = int(input('enter the number: '))
list = []

def isprime (n):
    i = 1
    while i < n:
        i += 1
        if n % i == 0:
            return n == i

for x in range(1,a):
    if(isprime(x)):
        if a % x == 0:
            print(x)
            a /= x
            if a % x == 0:
                print(x)