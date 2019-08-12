import re
# \d is equivalent to [0-9].
p=re.compile('\d')
print(p.findall("Iam going to my village on 14th 08 2019 and agin going to vinayaka chavithi on next month 2nd 09 22019"))

# \d+ will match a group on [0-9], group of one or greater size
q=re.compile('\d+')
print(q.findall("Iam going to my village on 14th 08 2019 and coming back by 15th 08 2019 "))