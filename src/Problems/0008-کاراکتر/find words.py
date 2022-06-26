list1 = []
list2 = []
list3 = []
list10 = []
a = input()
import urllib.request
fp = urllib.request.urlopen(a)
mybytes = fp.read()
mystr = mybytes.decode("utf8")
fp.close()
from bs4 import BeautifulSoup
soup = BeautifulSoup(mystr, 'html.parser')
words = soup.get_text()
words_split = words.split(' ')
for x in words_split:
    u = 0
    if x in list1:
        words_split.remove(x)
    else:
        for o in words_split:
            if x == o:
                u += 1
        list1.append(x)
        list2.append(u)
for hg in range(0,len(list1)):
    list3.append((list1[hg] , list2[hg]))
sorts = sorted(list3, key=lambda tup: -1*tup[1])
print(sorts[0:10])