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
