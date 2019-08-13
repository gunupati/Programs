import re
import urllib
import urllib.request
sites='google rediff'.split()
print(sites)
for i in sites:
    print('searching',i)
    u=urllib.request.urlopen('http://'+i+'.com')
    text=u.read()
    title=re.findall('<title>.*</title>',str(text),re.I)
    print(title[0])