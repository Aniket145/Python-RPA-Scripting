#working of single thread
from threading import*
import time
class Mythread:

    def tasks(self):
        self.task1()
        self.task2()
        self.task3()
    def task1(self):
        print("step1 of my problem")
        time.sleep(5)
        print("Completed")

    def task2(self):
        print("step2 of my problem")
        time.sleep(5)
        print("Completed")

    def task3(self):
        print("step3 of my problem")
        time.sleep(5)
        print("Completed")
obj = Mythread()
t = Thread(target=obj.tasks)
t.start()
