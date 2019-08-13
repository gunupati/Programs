import re
mob=input('please enter a mobile num')
a=re.fullmatch('[6-9][0-9]{9}',mob)
if a!=None:
    print('Matched')
else:
    print('Not Matched')
