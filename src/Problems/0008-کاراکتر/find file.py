import urllib.request
from collections import Counter
list1 = []
list = []
a = input()
fhand = urllib.request.urlopen(a)
for line in fhand: 
    list.append(line.decode().split())
o = 0
while o < len(list):
	for x in list[o]:
		list1.append(x)
	o += 1
print(Counter(list1).most_common(10))