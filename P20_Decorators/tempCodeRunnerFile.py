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