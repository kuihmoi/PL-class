# basic decorator that prints a message before and after a function runs
def decorator(f):
    def wrapper():
        #defining inner wrapper that adds extra behavior
        print("this is a message before the function is called")
        f()
        print("this is a message after the function is called")
    return wrapper

@decorator
def my_function():
    print("this is the function being called.")

my_function()

# fucntions often takes argument, so decorator need to handle those arguments
# decorator that logs the argument passed to a function
def log_arguments(func):
    '''
    Decorator to log the arguments passed to a function.
    '''
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__} with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

@log_arguments
def add(a, b):
    '''
    Function to add two numbers.
    '''
    return a + b

result = add(5, 3)  # Output: calling add with arguments: (5, 3) and keyword arguments: {}
print(f"Result: {result}")  # Output: Result: 8

# preserve metadata using functools.wraps
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("after the function call")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    '''
    This functions says hello to the user.
    '''
    print(f"Hello, {name}!")

print(say_hello("John"))
print(f"function name: {say_hello.__name__}")  # Output: function name: say_hello
print(f"function doc: {say_hello.__doc__}")  # Output: function docstring: This functions says hello to the user.


from functools import wraps
# decarotor that accepts its own parameter
# decorator that repeats a functions execution a specified number of times
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
            return None
        return wrapper
    return decorator

@repeat(3)
def say_something(message):
    print(message)
    return message

say_something("Hello, World!")  # Output: Hello, World! (printed 3 times)

# decorator that measures the execution time of a function
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function(n):
    time.sleep(n)  # Simulate a slow function
    return n * 2

result = slow_function(2)  # Output: Function 'slow_function' executed in 2.0000 seconds
print(f"Result: {result}")  # Output: Result: 4

# can apply multiple decorators to a single function
# chaining multiple decorators
import time
from functools import wraps
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def log_arguments(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Arguments for {func.__name__}: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

@timer
@log_arguments
def compute_sum(n):
    return sum(range(n))

result = compute_sum(1000000)
print(f"Sum: {result}")

# decorator that logs functions calls
# logging decorator

import logging
import time
from functools import wraps

logging.basicConfig(filename='App_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_to_file(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            end_time = time.time()
            logging.info(f"Function '{func.__name__}' executed successfully in {end_time - start_time: .4f} seconds.")
            return result
        except Exception as e:
            logging.error(f"Function '{func.__name__}' failed with error: {e}")
            raise
        finally:
            end_time = time.time()
            logging.info(f"Function '{func.__name__}' finished execution in {end_time - start_time: .4f} seconds.")
    return wrapper

@log_to_file
def divide(a, b):
    return a / b

try:
    print(divide(10, 2))
    print(divide(10, 0))
except ZeroDivisionError as e:
    print(f"An error occured: {e}")

# decorator to count how many times a function is called
# class_Based Decorator
from functools import wraps

class CallCounter:
    def __init__(self, func):
        wraps(func)(self)
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Function {self.__name__} called {self.count} times")
        return self.__wrapped__(*args, ** kwargs)
    
@CallCounter
def multiply(a,b):
    return a * b

print(multiply(2, 3))
print(multiply(4, 5))