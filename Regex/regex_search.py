import re
text='iam mahesh reddy my Age 27 and my bay age is 22'
pattern=r'([A-Za-z]+) (\d+)'
print(re.match(pattern,text))