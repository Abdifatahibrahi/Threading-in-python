import time
from threading import Thread

class Hi(Thread):
    def run(self):
        for i in range(10):
            print('Hi')
            time.sleep(1)


class Hello(Thread):
    def run(self):
        for i in range(10):
            print("Hello")
            time.sleep(1)


c1 = Hi()
c2 = Hello()

c1.start()
c2.start()
c1.join()
c2.join()

print('Bye')