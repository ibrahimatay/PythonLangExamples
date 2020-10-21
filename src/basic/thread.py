# https://redislabs.com/blog/async-await-programming-basics-python-examples/
# https://gist.github.com/miguelgrinberg/f15bc03471f610cfebeba62438435508

import threading

def worker(name,volume):
	for index in range(volume):
		print("worker name:{0} index:{1}".format(name,index))

threads = []
for i in range(100):
    t1 = threading.Thread(target=worker, args=('t1',i,))
    threads.append(t1)
    t1.start()

    t2 = threading.Thread(target=worker, args=('t2',i,))
    threads.append(t2)
    t2.start()