n = int(input("Enter a number: "))
is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            is_prime = False
            break

print(f"{n} is a Prime Number" if is_prime else f"{n} is not a Prime Number")

