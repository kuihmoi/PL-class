def p(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False 
    return True

n2 = int(input("Enter a number: "))
if p(n2):
    print(f"{n2} is a prime number.")
else:
    print(f"{n2} is not a prime number.")