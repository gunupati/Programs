import threading
def cube(a):
	print('Print the cube value {}'.format(a*a*a))

def square(a):
	print('Print the squarevalue {}'.format(a*a))

if __name__=="__main__":
	t1=threading.Thread(targer=cube,name=t1,args=(10))
	t1=threading.Thread(targer=square,name=t1,args=(10))
	

	t1.start()
	t2.start()
	

	t1.join()
	t2.join()
	
	print("Done")
