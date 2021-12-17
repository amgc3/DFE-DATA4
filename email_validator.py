import re

def email_validator(email):
    """
    function to validate email address
    """
    regex = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    # check if email address is valid
    if re.match(regex, email):
        return True
    else:
        return False

def is_valid(file_name):
    """
    function that takes email addresses from a file and prints  valid or invalid
    """
    try:
        with open(file_name) as f:
            data = f.readlines()
            print(data)
    except FileNotFoundError:
            print("File not found")
            return

    for email in data:
        if email_validator(email):
            print(email)
        else:
            print('Invalid email: ' + email)

is_valid('./emails.txt')