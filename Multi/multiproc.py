import multiprocessing
import time
import math
import sys


sys.set_int_max_str_digits(1000000)

def fact(number):
    print(f"Factorial of {number} is {math.factorial(number)}")
    
if __name__=="__main__":
    
    
    numbers=[5,6,7,8,9,10]
    start=time.time()
    for number in numbers:
        p=multiprocessing.Process(target=fact, args=(number,))
        p.start()
        p.join()
        
    print("Done")