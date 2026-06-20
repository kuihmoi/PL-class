from utils.string_utils import to_uppercase, reverse_text
from utils.number_utils import is_even, square
from utils.math.calculation import factorial
from utils.math_utils import PI
text = 'python'

print(f"Original text: {text}")
print(f"Uppercase: {to_uppercase(text)}")
print(f"Reversed: {reverse_text(text)}")

n = 7
print(f"number : {n}")
print(f"Is {n} even? {is_even(n)}")

print(f"factorial of {n} is {factorial(n)}")

print(f"Value of PI: {PI}")