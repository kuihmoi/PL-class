# 1. basic decorator syntax
# A simple decorator that wraps a function with a header/footer announcement.

def announce(func):
    """Prints a header/footer around any sales report function"""
    def wrapper():
        print("-" * 40)
        print(f" Report: {func.__name__}")
        print(f" Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print("-" * 40)
        func()
        print("-" * 40)
    return wrapper

@announce
def sales_summary():
    total = sum(r["units"] * r["price"] for r in SALE_RECORDS)
    print(f" Total Revenue: ${total:,.2f}")

# @announce is identical to writing: sales_summary = announce(sales_summary)
sales_summary()
###########################################################################################

# 2. decorators with arguments
# write a more flexible version of the announce decorator that can work with any function signature, not just no-argument

def announce_with_args(func):
    """Works on functions that accept any arguments"""
    def wrapper(*args, **kwargs):
        print(f"[START] Calling '{func.__name__}' ...")
        result = func(*args, **kwargs)
        print(f"[END]  '{func.__name__}' finished.")
        return result
    return wrapper

@announce_with_args
def total_revenue_by_product(product):
    total = sum(
        r["units"] * r["price"]
        for r in SALES_RECORDS
        if r["product"] == product
    )
    print(f" Revenue for '{product}': ${total:,.2f}")
    return total

@announce_with_args
def units_sold(product, region):
    units = sum(
        r["units"]
        for in SALES_RECORDS
        if r ["product"] == product and r["region"] == region
    )
    print(f" Units of '{product}' in '{region}': {units}")
    return units

total_revenue_by_product("Laptop")
units_sold("Phone", "North")
###########################################################################################

# 3. preserving function metadata
# write a decorator that does not use @functools.wraps and show how it causes the decorated function
# Then, write a corrected version of the decorator that uses @functools.wraps tp preserve the metadata

def bad_decorator(func):
    """Decorator WITHOUT @wraps - metadata is lost"""
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def good_decorator(func):
    """Decorator WITH @functools.wraps - metadata is preserved"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def report_without_wraps():
    """Returns the numbers of sales records"""
    return len(SALES_RECORDS)

@good_decorator
def report_with_wraps():
    """Returns the number of sales records"""
    return len(SALES_RECORDS)

###############33 TAK HABIS LAGI ##################

###########################################################################################

# 4. decorators with parameters
# write a decorator factory that takes an argument (e.g, number of repetitions)
# and returns a decorator that applies taht behavior to the decorated function

def repeat(times):
    """Decorator factory: runs teh decorated function 'times' times"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for i in range(1, times + 1):
                print(f" Run{i}/{times}:")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def print_top_product():
    top = max(SLAE)