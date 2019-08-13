import re
f1=open('mobile_nums.txt','r')
f2=open('extracted_mobile_list','w')
for i in f1:
    lists=re.findall('[6789][0-9]{9}',i)
    for j in lists:
        f2.write(j+'\n')
f1.close()
f2.close()