c = int(input('enter the numebr: '))

def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n -2)

a = fibonacci (c)
y = 1
while y < c:
    a = fibonacci (y)
    print(a)
    y += 1