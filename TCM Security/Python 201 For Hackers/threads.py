#!/usr/bin/env python3

import threading, time
from datetime import datetime

def sleeper(i):
    print(f"Hello from {i}!")
    time.sleep(i)
    print(f"Goodbye from {i}!")

print(datetime.now().strftime("%H:%M:%S"))
# In this setting, execution will take six seconds, because the functions are
# called consecutively, not parallel to each other.
sleeper(0)
sleeper(1)
sleeper(2)
sleeper(3)
print(datetime.now().strftime("%H:%M:%S"))

# ---

print(datetime.now().strftime("%H:%M:%S"))
# In this setting, execution will take three seconds, because the functions are
# called concurrently, parallel to each other.
threading.Thread(target=sleeper, args=(0,)).start()
threading.Thread(target=sleeper, args=(1,)).start()
threading.Thread(target=sleeper, args=(2,)).start()
threading.Thread(target=sleeper, args=(3,)).start()
print(datetime.now().strftime("%H:%M:%S"))

# ---

# Here the functions are called concurrently, but only after a pre-defined
# time.
print(datetime.now().strftime("%H:%M:%S"))
threading.Timer(0, sleeper, [0]).start()
threading.Timer(1, sleeper, [1]).start()
threading.Timer(2, sleeper, [2]).start()
threading.Timer(3, sleeper, [3]).start()
print(datetime.now().strftime("%H:%M:%S"))

# ---

# The two functions can basically "communicate" by using this global variable.
stop = False

def input_thread():
    global stop
    while True:
        user_input = input("Should we stop?: ")
        print(f">> User says {user_input} ..")
        if user_input == "yes":
            stop = True
            break

def output_thread():
    global stop
    count = 0
    while not stop:
        print(count)
        count += 1
        time.sleep(1)

threading.Thread(target=input_thread).start()
threading.Thread(target=output_thread).start()

# ---

data_lock = threading.Lock()
data = [x for x in range(1000)]

def consume_thread():
    global data_lock, data
        while True:
            data_lock.acquire()
            if len(data) > 0:
                # As long as there are values in the list, print the current value
                # that's at the end of the list and pop - remove - it afterwards.
                print(data.pop())
            data_lock.release()

# Starting these without a lock might introduce a race condition, meaning that
# similar threads are trying to pop the same list element, leading to issues.
# Starting these with a thread means that the elements are printed and removed
# from the list in consecutive order.
threading.Thread(target=consume_thread).start()
threading.Thread(target=consume_thread).start()
threading.Thread(target=consume_thread).start()
