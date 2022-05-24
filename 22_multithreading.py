'''
when we break down a process, each parts will be known as thread which runs simultaneously
suppose if a function takes 10s, instead of waiting, the processor can start running on other thread parallelly
'''

from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello...")
            sleep(0.5)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi...")
            sleep(0.5)

t1=Hello()            
t2=Hi()

#run in sequence, single thread, only main thread
# t1.run()
# t2.run()

#run in parallel, multi thread, 3 threads, main, t1, t2
t1.start() #start instead of run... must be 'run', not any other name
t2.start()

print("voilaa") #this will be printed since it is running on main thread, and not on t1 or t2