import random
a=[1,3,5,7,9,11,13,15]
b=[]
for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a)):
            b.append((a[i],a[j],a[k]))
            # if a[i]+a[j]+a[k]==30:
            #     print(a[i],a[j],a[k])
print(len(b))