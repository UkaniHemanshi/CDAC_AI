# Create a decorator function to log message to a log file

import logging
import time

logging.basicConfig(filename="decoratorExampleLog.log",
                    level=logging.INFO,
                    filemode="w",
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    datefmt="%d/%m/%Y %I:%M:%S %p")

def decor1(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"Function name is {func.__name__}.")
        return result
    return wrapper

def decor2(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try :
            result = func(*args, **kwargs)
            return result
        finally:
            end_time = time.time()
            exec_time = end_time - start_time
            logging.info(f"Function {func.__name__} took {exec_time:.4f} seconds to execute")
    return wrapper


@decor2  # decorator 2 which print function execution time into log file
@decor1  # decorator 1 which print name of function into log file
def decor_log_fun(n):
    time.sleep(n)
    print(f'This is decor_log_function which contain both used 1. decorator 2. logging concepts')

print(decor_log_fun(3))
