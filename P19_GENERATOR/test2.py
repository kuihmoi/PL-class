def number_generator():
    yield 1
    yield 2
    yield 3

gen = number_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

for i in number_generator():
    print(i)  # Output: 1, 2, 3

# generators that yields even numbers up to specified limit
def even(L):
    n = 0
    while n < L:
        yield n
        n += 2

for i in even(10):
    print(i)  # Output: 0, 2, 4, 6, 8

# generator expression to create square of numbers
squares = (x**2 for x in range(10)) #cretaes generator without defining a function
print(list(squares)) # wiht list it exhausts the generators

square = (x**2 for x in range(10))
for i in square:
    print(i)  # Output: 0, 1, 4, 9, 16, 25, 36, 49, 64, 81

# generator that yields fibonacci numbers up to specified limit
def fib(L):
    a, b = 0, 1
    while a < L:
        yield a
        a, b = b, a + b

x = fib(10)
print(list(x))

# generator for an infinite sequence of prime numbers with a way to control output
def is_prime(n):
    if n <= 1:
        return False  #less than 2 cannot be prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True #otherwise true

def prime_generator():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

p = prime_generator()
for _ in range(10):
    print(next(p))  # Output: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29

# generator pipeline
def integers(n):
    for i in range(1, n):
        yield i

def filter_odds(n):
    for i in n:
        if i % 2 != 0:
            yield i

def squared(n):
    for i in n:
        yield i**2

# 3 functions chained together to create a pipeline
# pipeline - process data lazily
a = squared(filter_odds(integers(10)))
print(list(a))  # Output: [1, 9, 25, 49, 81]

def sub_generator():
    yield 'a'
    yield 'b'
    yield 'c'

def main_generator():
    yield 'start'
    yield from sub_generator()  # Delegates to sub_generator
    yield 'end'

for i in main_generator():
    print(i)  # Output: start, a, b, c, end

# generator that receives input via send() to modify its behavior
def counter():
    count = 0
    while True:
        received = yield count
        if received is not None:
            count = received
        else:
            count += 1

gen = counter()
print(next(gen))  # Output: 0
print(gen.send(5))  # Output: 5 # it means updating the count here with send()
print(next(gen))  # Output: 6       
print(next(gen))  # Output: 7

# generator to read a large text file line by line
def read(file_path):
    try:
        with open(file_path, 'r') as f:
            for line in f:
                yield line.strip() #produce each line without trading new line
    except FileNotFoundError:
        print("File not found")

for i in read("python.txt"):
    print(i)