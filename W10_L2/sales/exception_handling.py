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
        df = pd.read_csv('sales/data/non_existent_file.csv')
    except Exception as e:
        print("An error occurred, but we handle it, program keeps running.")

    # loading the REAL sales file:
    try:
        df = pd.read_csv(DATA_FILE)
        print(f"Loaded {len(df)} rows successfully.")
    except Exception:
        print("Failed to load the sales data file.")

basic_try_except()
###########################################################################################################################

# 2. HANDLING SPECIFIC EXCEPTIONS

def specific_exceptions() -> None:
    # A) FileNotFoundError:
    try:
        df = pd.read_csv('sales/data/non_existent_file.csv')
    except FileNotFoundError as e:
        print(f"File not found: '{e.filename}'")

    # B) ValueError (bad string-to-number conversion)
    bad_price = "not_a_number"
    try:
        price = float(bad_price)
    except ValueError as e:
        print(f"Cannot convert '{bad_price}' to float.")

    print("C) ZeroDivisionError:")
    units = 0
    try:
        avg = 5000 / units
    except ZeroDivisionError:
        print(f"Cannot compute average - units sold = {units}.")

specific_exceptions()

###########################################################################################################################
# 3. MULTIPLE EXCEPTION HANDLING

def multiple_exceptions() -> None:
    # reads a CSV file, computes the sum of a specified column, and handles exceptions such as missing files, missing columns and invalid data types.
    def load_column_total(filepath: str, column: str) -> float | None:
        try:
            df = pd.read_csv(filepath)
            return float(df[column].sum())
        except FileNotFoundError:
            print(f"File '{filepath}' does not exist.")
        except KeyError:
            print(f"Column '{column}' not found in CSV.")
        except (TypeError, ValueError) as e:
            print(f"Data type problem: {e}")
        return None
    
    print("Test 1: wrong file path:")
    load_column_total('sales/data/ghost.csv', 'Units')

    print("Test 2: wrong column name:")
    load_column_total(DATA_FILE, 'NonExistentColumn')

    print("Test 3: valid file and column:")
    result = load_column_total(DATA_FILE, 'Units')
    if result is not None:
        print(f"Total Units sold: {result:.0f}")

multiple_exceptions()
###########################################################################################################################
# 4. THE ELSE CLAUSE: runs ONLY when no exceptions was raised in "try" block.

def else_clause() -> None:
    # loads a CSV file, calculates new Reveneue column from Units and Price, computes the total revenue, and handle missing file errors using try-except-else.
    def load_and_summarise(filepath: str) -> None:
        try:
            df = pd.read_csv(filepath)
        except FileNotFoundError:
            print(f"Could not find file: {filepath}")
        else:
            # This block only runs when pd.read_csv() succeeded
            df['Revenue'] = df['Units'] * df['Price']
            total = df['Revenue'].sum()
            print(f"{len(df)} rows loaded. Total Revenue: ${total:,.0f}")

    print("Missing file (else does NOT run):")
    load_and_summarise('sales/data/missing.csv')

    print("Real file (else DOES run):")
    load_and_summarise(DATA_FILE)

else_clause()
###########################################################################################################################
# 5. THE FINALLY CLAUSE: ALWAYS runs, whether an exception occured or not

def finally_clause() -> None:
    # a function that processes a CSV report using try-except-finally, handles missing files and missing columns, and demonstrates that the finally block always executes.
    def process_report(filepath: str) -> None:
        print(f"[START] Processing: '{filepath}'")
        df = None
        try:
            df = pd.read_csv(filepath)
            _ = df["NonExistentRevenue"]
        except FileNotFoundError:
            print("[ERROR] File not found.")
        except KeyError as e:
            print(f"[ERROR] Missing column: {e}.")
        finally:
            if df is not None:
                print(f"[FINALLY] {len(df)} rows were loaded - releasing resources.")
            else:
                print("[FINALLY] No data was loaded - cleanup complete.")
            print("[FINALLY] This block ALWAYS runs.\n")

    print("Test 1: file loads but column is missing (finally still runs):")
    process_report(DATA_FILE)

    print("Test 2: file is missing entirely (finally still runs):")
    process_report('sales/data/missing.csv')

finally_clause()
###########################################################################################################################
# 6. RAISING EXCEPTIONS: to signal that something is wrong to the CALLER of your function

# 7. CUSTOM EXCEPTIONS: Define your own exception classes by inheriting from Exception.
