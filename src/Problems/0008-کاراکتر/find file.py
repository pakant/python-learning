import urllib.request
from collections import Counter
list1 = []
list = []
a = input()
fhand = urllib.request.urlopen(a)
txt = fhand.readlines().decode('.')
print(txt)
print(fhand)
# for line in fhand: 
#     list.append(line.decode('.').split())
# o = 0
# while o < len(list):
# 	for x in list[o]:
# 		list1.append(x)
# 	o += 1
# counters = (Counter(list1).most_common(10))
# print(counters)