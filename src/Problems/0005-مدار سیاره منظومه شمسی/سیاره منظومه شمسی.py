dictinary = {1:'Mercury' , 2:'Venus' , 3:'Erath' , 4:'Mars' , 5:'Jupiter' , 6:'Saturn' , 7:'Uranus' , 8:'Neptune'}
list = [110 , 150 , 230 , 780 , 1430000000 , 2880000000 , 4500000000]
list87=[]
for x in list:
    if x % 60 == 0:
        hg = x / 60
        list87.append(int(hg) * '-')
        print()
    else:
        yt = x / 60
        list87.append(int((yt) + 1) * '-')
y = 0
u = 2
while y<7:
    if y == 0:
        print('sun - ' , dictinary.pop(1))
        print()
    print('sun' , list87[y] , dictinary.pop(u))
    y += 1
    u += 1
    print()