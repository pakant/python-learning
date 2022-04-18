a = int(input('enter the number in range 1 to 10: '))
dictinary = {1:'one' , 2:'two' , 3:'three' , 4:'four' , 5:'five' , 6:'six' , 7:'seven' , 8:'eight' , 9:'nine' , 10:'ten'}
if a in dictinary:
    print(dictinary.pop(a))
else:
    print(a , 'is not in range 1 to 10')