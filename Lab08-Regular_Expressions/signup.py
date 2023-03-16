""" Harsha CS 211
    Regular Expressions """

import re


def validate_email(email: str):

    regex = re.fullmatch("^[A-Za-z][A-Za-z0-9]+@[a-z]+\.(com|edu)", email)
    return bool(regex)


def validate_pass(password: str):

    regex = re.fullmatch("(?=.*\d)(?=.*\W).{10,}", password)
    return bool(regex)


if __name__ == "__main__":

    email = input("Provide an email address:")

    while not validate_email(email):
        email = input("Invalid email, provide a different one:")

    password = input("Input your password:")

    while not validate_pass(password):
        password = input("Invalid password, provide a different one:")
    print("Signup Successful")
