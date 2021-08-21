from threading import Timer


def show():
    print('Hello World.!')


t1 = Timer(3.0, show)
t1.start()
