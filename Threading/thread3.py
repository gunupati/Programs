import threading

# global variable x
x = 0

def increment():
	"""
	function to increment global variable x
	"""
	global x
	x += 1

def thread_task(lock):
	"""
	task for thread
	calls increment function 100000 times.
	"""
	for _ in range(100000):
		lock.acquire()
		increment()
		lock.release()

def main_task():
	global x
	# setting global variable x as 0
	x = 0

	# creating a lock
	lock = threading.Lock()

	# creating threads
	t1 = threading.Thread(target=thread_task, args=(lock,))
	t2 = threading.Thread(target=thread_task, args=(lock,))

	# start threads
	t1.start()
	t2.start()

	# wait until threads finish their job
	t1.join()
	t2.join()

if __name__ == "__main__":
	for i in range(10):
		main_task()
		print("Iteration {0}: x = {1}".format(i,x))



# Iteration 0: x = 200000
# Iteration 1: x = 200000
# Iteration 2: x = 200000
# Iteration 3: x = 200000
# Iteration 4: x = 200000
# Iteration 5: x = 200000
# Iteration 6: x = 200000
# Iteration 7: x = 200000
# Iteration 8: x = 200000
# Iteration 9: x = 200000