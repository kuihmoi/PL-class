import os
import traceback
from contextlib import suppress, contextmanager
import pandas as pd

DATA_FILE = 'sales/data/sales.csv'

# 1. BASIC TRY-EXCEPT BLOCK
# Write a code to try to load a CSV file that does NOT exist, and catch the resulting exception to print a user-friendly message without crashing the program.
# Then, write another try-except block to load the REAL sales file and print a success message if it loads correctly.
def basic_try_except():
    # loading a file that does not exist
    try:
        # df = pd.read_csv('sales/data/non_existent_file.csv')
        df = pd.read_csv('data/sales.csv')
    except Exception as e:
        print("An error occurred, but we handle it, program keeps running.")

    # loading the REAL sales file:
    try:
        df = pd.read_csv(DATA_FILE)
        print(f"Loaded {len(df)} rows successfully.")
    except Exception:
        print("Failed to load the sales data file.")

basic_try_except()