import time
def countdown(n):
    while n > 0:
        yield n
        n -= 1

tasks = [countdown(10), countdown(5)]

# c1 = countdown(10)

# print(next(c1))
# print(next(c1))

print(len(tasks))
print("------")

while tasks:
    task = tasks[0]
    tasks.remove(task)
    try: 
        x = next(task)
        time.sleep(1)
        print(x)
        tasks.append(task)
        

        
    except StopIteration:
        print("Task finished")

print("------")

print(len(tasks))