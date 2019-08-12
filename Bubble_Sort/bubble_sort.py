def bubble_sort(a):
    for i in range(len(a)):
        for j in range(0,len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

a=[1,4,2,56,3453,5435,43,3543]
bubble_sort(a)
print ("Sorted array is:")
for i in a:
    print(i)



# Sorted array is:
# 1
# 2
# 4
# 43
# 56
# 3453
# 3543