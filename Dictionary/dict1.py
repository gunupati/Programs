a={}
n=int(input("Please enter the value of n:"))
for i in range(n):
    name=input("please enter the name ")
    marks=input("Enter the % of marks")
    a[name]=marks
print('name of the student','\t','% of marks')
for x in a:
    print('\t',x,'\t\t',a[x])
