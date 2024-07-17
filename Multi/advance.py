from concurrent.futures import ThreadPoolExecutor
import time 
def print_number(number):
    time.sleep(1)
    return f"Threads: {number}"

numbers=[1,2,3,4,5,6,7,8,9,10]
with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_number, numbers)
for result in results:
        print(result)
        time.time()
        
#threadPoolExecutor is a class that is used to run multiple threads concurrently.
#ProcessPoolExecutor is a class that is used to run multiple processes concurrently.