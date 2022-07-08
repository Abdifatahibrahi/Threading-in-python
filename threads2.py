import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor


def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f"Hello, {user_input}"
    print(greet)
    print(f"ask_user, {time.time() - start}")

    
def complex_calculation():
    start = time.time()
    print('Started calculating...')
    [x**2 for x in range(20000000)]
    print(f"complex_calculation, {time.time() - start}")


start = time.time()
ask_user()
complex_calculation()
print(f"Total time, {time.time() - start}")

with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(ask_user)
    pool.submit(complex_calculation)

print(f"Two thread: {time.time() - start}")

