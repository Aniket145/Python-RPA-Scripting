from threading import *
from time import *


class producer:
    def __init__(self, lock):
        self.lst = []
        self.dataproduce = False
        self.lock = lock

    def produce(self):
        for i in range(1, 11):
            self.lock.acquire()  # acquire lock
            self.lst.append(i)
            sleep(1)
            print("Item produced........")
            self.lock.release()  # release lock
        self.dataproduce = True


class consumer:
    def __init__(self, prod, lock):
        self.prod = prod
        self.lock = lock

    def consume(self):
        while self.prod.dataproduce == False:
            self.lock.acquire()  # acquire lock
            print((self.prod.lst))
            self.lock.release()  # release lock
            sleep(0.1)
            print("C")


lock = Lock()  # create a lock
p = producer(lock)
c = consumer(p, lock)

t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)
t1.start()
t2.start()
