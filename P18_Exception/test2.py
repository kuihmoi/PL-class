# try block that contains code that might raise an exception

# 1. handle a division by 0
try:
    x = 10 / 0
except  ZeroDivisionError as e:
    # instead of crashing we handle the error here
    print("Error: Division by Zero", e)
    print("Error:", e) # even if we dont write division by zero it will print the same

# can catch exception to handle different error appropriately 
# 2. Handling Specific Exceptions

try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    print(f"You entered: {number}")
except ValueError:
    # if user input something else (invalid number)
    print("That's not a valid number!")

# 3. Handle Multiple Exception Handling

try:
    num = int(input("Enter a number: "))
    denom = int(input("Enter a denominator: "))
    result = num / denom
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter a valid integer.")

# OR

try:
    num = int(input("Enter a number: "))
    denom = int(input("Enter a denominator: "))
    result = num / denom
    print(f"The result is: {result}")
except (ValueError, ZeroDivisionError):
    print("Error Occured.")

# 4. The "else" Clause
# runs if no exception is raised in the try block
# useful for code that you excecute and success
try:
    with open("number.txt", 'r') as file:
        number = int(file.read().strip())
except FileNotFoundError:
    print("File not found. Please create 'number.txt' with a number")
    exit(1)
except ValueError:
    print("Error: File does not contain a valid number.")
else:
    # no exception occurs, else block runs successfully
    print(f"File read successfully. {number}")
    exit(1)

# 5. The "finally" clause
# runs regardless of whether an exception was raised or not
try:
    file = open("number.txt", 'r')
    content = file.read()
    number = int(content.strip())
except FileNotFoundError:
    print("File not found. Please ensure the file exists")
except ValueError:
    print("Invalid number format. Please ensure the file has a number")
else:
    print("The number is: ", number)
finally:
    # we can have another try here (nested try, except)
    # ensure the file is closed even if we have an error
    try:
        file.close()
        print("File closed successfully.")
    except NameError:
        print("File was never opened, so it cannot be closed")

# 6. Raise Exceptions, raising exception intentionally
try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ValueError("You must be at least 18 years old.")
except ValueError as e:
    print(f"Error: {e}")
else:
    print("Access granted.")

# 7. Custom Exceptions
# you can define custom exceptions classes by inheriting from the built in
# class, useful for specific error types in your application  

# this class is a custom exception class inheriting from exception
class InsufficientFundsError(Exception):
    """Custom exception for insufficient account balance"""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            #raise insufficient error if withdrawal exceeds balance
            raise InsufficientFundsError(f"Cannot withdraw {amount:.2f}. Current balance is {self.balance}")
        self.balance -= amount
        return self.balance
    
# the custom exception here
try:
    account = BankAccount(100)
    print(f"Initial balance: {account.balance: .2f}")
    account.withdraw(50)
except InsufficientFundsError as e:
    print(f"Error: {e}")
else:
    print(f"Withdrawal successful. New balance: {account.balance:.2f}")

# 8. Context Managers and Exception Handling (complex topic)
# creating custom context manager for timing code execution

import time
from contextlib import contextmanager
@contextmanager
def timer(description):
    #measures execution time of block code 
    start = time.time()
    try:
        yield
    # catches exceptions, lock them and re-raise
    except Exception as e:
        print(f"Error in {description}: {e}")
    # calculates and prints the elapsed time
    finally:
        elapsed = time.time() - start
        print(f"{description} took {elapsed:.2f} seconds")

try:
    with timer("Division Operations"):
        result = 10 / 0
except ZeroDivisionError as e:
    # called by both context manager and outer exception
    print(f"Caught error: {e}")

with timer("Successful Operation"):
    total = sum(range(1000000))
    print(f"Total: {total}")

# 9. Catching Exceptions with no specific type (Bare Except)
# try catch any error during division
try:
    user_input = input("Enter a number: ")
    result = 10 / int(user_input)
    print(f"Result: {result}")
except:
    print("Something went wrong!")

# 10. Error Handling and Logging
import csv
import logging # record success and errors called app.log

logging.basicConfig(
    filename = 'app.log',
    level = logging.INFO,
    format = "%(asctime)s = %(levelname)s - $(message)s",
)

def process_csv(file_path):
    """
    Process a CSV file with error handling and logging
    """
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            total = 0
            for row in reader:
                if len(row) < 2:
                    raise ValueError(f"Invalid row format: {row}")
                value = float(row[1])
                total += value
        logging.info(f"Successfully processed {file_path}. Total: {total}")
        return total
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except ValueError as e:
        logging.error(f"Value error: {e}")
        raise
    finally:
        logging.info(f"Finshed processing {file_path}")

try:
    with open("data2.csv", "w") as f:
        f.write("name, amount\n item1, 10 \n item2, 20 \n item3, 30")
    total = process_csv("data2.csv")
    print(f"Total amount: {total:.2f}")
except Exception as e:
    print(f"An error occured: {e}")
    logging.error(f"An error occured: {e}")

# 11. Assess Exception Information beyond the message
# want to assess of an attribute FileNotFoundError

import traceback
#try block try to attempt open file that does not exist and raise error FileNotFoundError
try:
    with open("nofile.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"Error message: {str(e)}")
    print(f"Error arguments: {e.args}")
    print(f"error number: {e.errno}")
    print(f"stack trace:")
    #printing full stack trace
    traceback.print_exc()