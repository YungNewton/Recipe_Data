def count_letters_digits(s):
    letters = sum(c.isalpha() for c in s)
    digits = sum(c.isdigit() for c in s)
    return (letters, digits)

# Test the function
print(count_letters_digits("Hello World! 123"))
