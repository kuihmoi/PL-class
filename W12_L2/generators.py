import csv
import itertools
import os
import random
from datetime import date, timedelta

# small in-memory dataset in form of dictionary
SAMPLE_SALES = [
    {"date": "2023-01-05", "product": "Laptop", "region": "North", "units": 3, "price": 999},
    {"date": "2023-01-08", "product": "Phone", "region": "South", "units": 10, "price": 499},
    {"date": "2023-01-12", "product": "Tablet", "region": "East", "units": 5, "price": 329},
    {"date": "2023-01-15", "product": "Monitor", "region": "West", "units": 7, "price": 249},
    {"date": "2023-02-03", "product": "Laptop", "region": "East", "units": 4, "price": 999},
    {"date": "2023-02-07", "product": "Phone", "region": "North", "units": 12, "price": 499},
    {"date": "2023-03-08", "product": "Phone", "region": "North", "units": 14, "price": 499},
    {"date": "2023-03-12", "product": "Tablet", "region": "West", "units": 9, "price": 329}
]

# 1) Functions vs Generator Functions
# Write a function that computes and returns a list of revenues for all sales records in one go
def get_all_revenues_list(sales_data):
    """Regular function, builds and returns teh ENTIRE list at once"""
    revenues = []
    for row in sales_data:
        revenues.append(row["units"] * row["price"])
    return revenues #all values exist in memory simultaneously

get_all_revenues_list(SAMPLE_SALES)

#convert this function into a generator


# 2) Generator function; yields one revenue at a time, pausing between each.
# write a generator function that computes and yields one revenue at a time, pausing after each yield until thenext values is requested
def revenue_generator(sales_data):
    """Generator function, yields ONE revenue, pauses then resumes"""
    for row in sales_data:
        yield row["units"] * rows["price"] # pause here; resume on next pull

gen = revenue_generator(SAMPLE_SALES)
print("\nGenerator function -> {type(gen)}")
print(" (No revenues computed yet, the function body hasn't run at all!)")

# Values are produced only when you iterate:
print("\nPulling values one at a time with next():")
print(f" next() call 1 -> ${next(gen):,}")
print(f" next() call 2 -> ${next(gen):,}")

#use a for-loop, which handles StopIteration automatically:
print("\nConsuming the rest with a for-loop:")
for rev in gen:
    print(f" ${rev:,}")

###########################################################################################
# 3) Generator for a Range with Step
# use gen() to print numbers from 0 to 4, then (tak habis)
for i in range(5):
    print(i)

for i in range(3, 8):
    print(i)

for i in range(1, 10, 2):
    print(i)
###########################################################################################

# define a generator function 'range_with_step(start, stop, step)' that yields integers from 'start' up to (but not including) 'stop', incrementing
# Then, demonstrate its usage by printing numbers from 1 to 4 with a step of 1, from 1 to 9 with a step of 2, every 3rd week of quarter (1 to 14)

def range_with_step(start, stop, step=1):
    """Yields integers from 'start' up to (not including) 'stop' by 'step'"""
    current = start
    while current < stop:
        yield current
        current += step

print("Sale IDs 1-4 (step=1):", list(range_with_step(1, 5)))

print("Sale IDs 1-4 (step=2):", list(range_with_step(1, 10, 2)))

print("Every 3rd week of a quarter:", list(range_with_step(1, 14, 3)))

print("Every 5th record index in our dataset:", list(range_with_step(0, 25, 5)))

# Generators are lazy, you don't have to consume all values.
print("\nLazy: generating sale IDs but stopping after the 3rd:")
id_gen = range_with_step(1001, 9999)
for _ in range(3):
    print(f" Sale #{next(id_gen)}")

###########################################################################################

# 4) Generator Expression
# use list comprehension to create a listt of revenues for all laptop sales
laptop_rev_list = [r["units"] * r["price"]
                    for r in SAMPLE_SALES if r["product"] == "Laptop"]
print(
    f"List comprehension -> {type(laptop_rev_list).__name__}: {laptop_rev_list}"
)

# Now rewrite this as generator expression, same syntax but with parentheses instead of brackets
laptop_rev_gen = (r["units"] * r["price"]
                   for r in SAMPLE_SALES if r["product"] == "Laptop")
print(f"Generator expression -> {type(laptop_rev_gen)}")

# sum(), max(), min(), all accept generators, no list needed
print(f"Total Laptop revenue: ${sum(laptop_rev_gen):,}")

# total revenue across all products in one line
total = sum(r["units"] * r["price"] for r in SAMPLE_SALES  if r["region"] == "North")
print(f"Total revenue (all products): ${total:,}")

# Filter + transforms in one expression
north_products = list(r["product"]
                      for r in SAMPLE_SALES if r["region"] == "North")
print(f"Products sold in North: {north_products}")
###########################################################################################

# 5) 