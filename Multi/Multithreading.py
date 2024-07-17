import threading
import time

def my_function():
    for i in range(5):
        print("Thread 1: ", i)
        time.time()
    
   
def printtime():
    for i in "abcde":
         print(i)
         time.time()
  
p1=threading.Thread(target=my_function)
p2=threading.Thread(target=printtime)
p1.start()
p2.start()
p1.join()
p2.join()
