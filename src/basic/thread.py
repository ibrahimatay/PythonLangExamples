import threading

def worker(name,volume):
	for index in range(volume):
		print("worker name:{0} index:{1}".format(name,index))

threads = []
for i in range(100):
    threading.Thread(target=worker, args=('t1',i,)).start()
    threading.Thread(target=worker, args=('t2',i,)).start()