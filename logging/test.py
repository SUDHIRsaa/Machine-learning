from logging.logger import logging

def add(a,b):
    
    logging.debug("This will getadddition  debugged")
    return a+b


logging.debug("This will get debugged")
add(1,2)