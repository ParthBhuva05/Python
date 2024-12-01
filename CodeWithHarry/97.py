# Multithreading in Python

# Multithreading is a technique in programming that allows multiple threads of execution to run concurrently within a single process. In Python, we can use the threading module to implement multithreading. In this tutorial, we will take a closer look at the threading module and its various functions and how they can be used in Python.


# Importing Threading

# We can use threading by importing the threading module.
# import threading


# Creating a thread

# To create a thread, we need to create a Thread object and then call its start() method. The start() method runs the thread and then to stop the execution, we use the join() method. Here's how we can create a simple thread.


# Functions

# The following are some of the most commonly used functions in the threading module:

# threading.Thread(target, args): This function creates a new thread that runs the target function with the specified arguments.

# threading.Lock(): This function creates a lock that can be used to synchronize access to shared resources between threads.


# Creating multiple threads

# Creating multiple threads is a common approach to using multithreading In Python. The Idea is to create a poot of worker threads and then assign tasks to them as needed. This allows you to take advantage of multiple CPU cores and process takes in parallel.






import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"sleeping for {seconds} seconds.")
    time.sleep(seconds)
    return seconds

def main():

    time1 = time.perf_counter()
    # Normal Code
    # func(4)
    # func(2)
    # func(1)


    # Same Code Using Threads
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    # Calculting Time
    time2 = time.perf_counter()
    print(time2 - time1)


def poolingDemo():
    with ThreadPoolExecutor() as executor:
    #     future1 = executor.submit(func, 3)
    #     future2 = executor.submit(func, 2)
    #     future3 = executor.submit(func, 4)

    #     print(future1.result())
    #     print(future2.result())
    #     print(future3.result())

        l = [3, 5, 1, 2]
        results = executor.map(func, l)
        for result in results:
            print(result)

poolingDemo()








