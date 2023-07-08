def count_letters_digits(s):
    letters = sum(c.isalpha() for c in s)
    digits = sum(c.isdigit() for c in s)
    return (letters, digits)

# Test the function
print(count_letters_digits("Hello World! 123"))


def validate_password(password):
    if len(password) < 8: 
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password): 
        return False
    if not any(char.islower() for char in password):
        return False
    if not password.isalnum():
        return False
    return True

# Test the function
print(validate_password("acab"))  # Output: False
print(validate_password("acaB27uo"))  # Output: True
print(validate_password("aca679B-$"))  # Output: False

def change_password(newpass, oldpasswords):
    # Check if the new password is equivalent to any of the old passwords
    if newpass in oldpasswords:
        return False

    # Check if the new password contains any 3 consecutive characters from any old passwords
    for oldpass in oldpasswords:
        for i in range(len(oldpass) - 2):  # subtract 2 to avoid out-of-range error
            if oldpass[i:i+3] in newpass:
                return False

    return True

# Test the function
print(change_password("James001", ["James003", "Hello111"]))  # Output: False
print(change_password("James001", ["Iron001", "helloA114599"]))  # Output: True
print(change_password("James001", ["ires0087"]))  # Output: False


def factorial(n):
    # Factorial of 0 is 1
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

# Test the function
print(factorial(0))  # Output: 1
print(factorial(1))  # Output: 1
print(factorial(7))  # Output: 5040


def fibonacci(n):
    # Initialize the Fibonacci sequence with the first two numbers
    fib_seq = [0, 1]

    # Generate the rest of the sequence
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])

    return fib_seq

# Test the function
print(fibonacci(5))  # Output: [0, 1, 1, 2, 3]
print(fibonacci(8))  # Output: [0, 1, 1, 2, 3, 5, 8, 13]
