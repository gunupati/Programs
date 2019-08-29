import os,sys
fname=input("Enter file name:")
if os.path.isfile(fname):
    print("File Exits:",fname)
    f=open(fname,'r')
else:
    print('File does not exist',fname)
    sys.exit(0)
print('The content of file is :')
data=f.read()
print(data)