dictionary = {1:'Mercury' , 2:'Venus' , 3:'Erath' , 4:'Mars' , 5:'Jupiter' , 6:'Saturn' , 7:'Uranus' , 8:'Neptune'}
list=[108200000,149600000,227900000,778600000,1433500000,2872500000,4495100000]
y = 2
print('sun - ',dictionary.pop(1))
for x in list:
    print('sun' , (int(x / 57900000) + 1) * '-' , dictionary.pop(y))
    y += 1