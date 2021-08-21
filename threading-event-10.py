from threading import Thread, Event
from time import sleep


def first(e1, e2):
    print('First is stating ...')
    e1.set()
    e2.wait()
    print('First is working ...')
    e1.clear()

def second(e2, e1):
    sleep(10)
    print('Second is stating ...')
    e2.set()
    e1.wait()
    print('Second is working ...')
    e2.clear()


e1 = Event()
e2 = Event()


t1 = Thread(target=first, args=(e1, e2))
t2 = Thread(target=second, args=(e2, e1))


t1.start()
t2.start()
