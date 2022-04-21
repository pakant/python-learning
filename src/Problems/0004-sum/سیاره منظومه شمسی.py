dictinary = {1:'Mercury' , 2:'Venus' , 3:'Erath' , 4:'Mars' , 5:'Jupiter' , 6:'Saturn' , 7:'Uranus' , 8:'Neptune'}
list = [108200000 , 149600000 , 227900000 , 778600000 , 1433500000 , 2872500000 , 4495100000]
print('sun - ',dictinary.pop(1))
y = 2
for x in list:
    print('sun' , (int(x / 57900000) + 1)* '-' , dictinary.pop(y))
    y += 1