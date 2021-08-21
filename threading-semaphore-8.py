from threading import Thread, Semaphore, BoundedSemaphore, current_thread
from time import sleep


num = 0

# lock = Semaphore(value=2) 
lock = BoundedSemaphore(value=2) 

def add():
    global num
    with lock:
        print(current_thread().getName())
        sleep(2)
        num += 1

    # lock.acquire()
    # print(current_thread().getName())
    # sleep(2)
    # num += 1
    # lock.release()


t1 = Thread(target=add)
t2 = Thread(target=add)
t3 = Thread(target=add)
t4 = Thread(target=add)
t5 = Thread(target=add)
t6 = Thread(target=add)


t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()


t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()


print(num)
print('Done ...')
