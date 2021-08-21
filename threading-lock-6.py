"""
    Race condition
    Thread safe
    Dead lock
    atomic
"""


from threading import Thread, Lock


num = 0 # shared resource

lock = Lock()


def add():
    global num
    with lock:
        for _ in range(100000):
            num += 1


def subtract():
    global num
    with lock:
        for _ in range(100000):
            num -= 1


t1 = Thread(target=add)
t2 = Thread(target=subtract)


t1.start()
t2.start()


t1.join()
t2.join()


print('Safe result :', num, 'be must is zero.')
print('Done ...')