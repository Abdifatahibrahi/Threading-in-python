from threading import Thread, Lock
import time
counter = 0

def increment_counter(lock):
    global counter
    lock.acquire()
    counter += 1
    print(f'The counter is {counter}')
    print("============")
    lock.release()

def square_counter(lock):
    global counter
    lock.acquire()
    counter = counter * counter
    print(f'The counter is {counter}')
    print("============")
    lock.release()

# if __name__ == '__main__':
for i in range(10):
            lock = Lock()
            thread1 = Thread(target=increment_counter, args=(lock,))
            thread2 = Thread(target=square_counter, args=(lock,))
            thread1.start()
            thread2.start()
            time.sleep(1)
