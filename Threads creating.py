#Method 1 to create a thread
from threading import *
def display(s):
    print(s)

for i in range(5):
    t = Thread(target=display,args=('Helllo',))
    t.start()

#METHOD 2 for creating a string
from threading import*
class MyThread(Thread):
    def __init__(self, s):
        Thread.__init__(self)
        self.s = s
    def run(self):
        print(self.s)


t1=MyThread('Hello')
t1.start()
t1.join()


from threading import *


class MyThread(Thread):
    def __init__(self, s):
        Thread.__init__(self)
        self.s = s

    def display(self, x, y):
        print(self.s)
        print(x, y)

obj = MyThread('Hello')
t1= Thread(target=obj.display, args=(1, 2))
t1.start()
t1.join()
