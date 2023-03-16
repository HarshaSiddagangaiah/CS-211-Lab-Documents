# Regular Expressions in Python
Python provides the "re" module to use regular expressions.

```python
import re
```

The following link has a very concise explanation of the use of the re module with some useful examples:

[W3Schools](https://www.w3schools.com/python/python_regex.asp).
For a more detailed explanation, refer to the following link:

[Python documentation](https://docs.python.org/3/howto/regex.html).

## Exercise - Sign-up interface
Suppose you are coding the sign-up interface for an application.

## Step 1
The program first prompts the user for an email address which will serve as the username.

The requirements for acceptable email addresses are as follows:

- Cannot start with a digit.
- Should only contain one @ symbol delimiting the username from the domain.
- Only accepted domains should end with '.edu' or '.com'.


Examples of incorrect email addresses:

- `2b_or_not_2b@gmail.com` -> starts with a digit.
- `jessic@warren@uoregon.edu` -> has multiple @ symbols.
- `john19@corporation.org` -> domain ending with '.org'.

Create a function called "validate_email" that receives an email address as an argument and returns True if it fulfills all the requirements for a correctly formated address, and False otherwise.

## Step 2
Once the email has been validated, the program should ask the user for a password.

The requirements for an acceptable password are as follows:

- Must contain at least 10 characters
- Must contain at least 1 digit
- Must contain at least one special symbol (non-alphanumeric)

Examples of non-acceptable passwords:

- `r3dc@t` -> not long enough
- `str@ngepl@net` -> does not contain digits
- `ic3br3ak3r` -> does not contain non-alphanumeric symbols

Create a function called `"validate_password"` that receives an password as an argument and returns True if it fulfills all the requirements for a correctly formated password, and False otherwise.

## Step 3
When you are done defining your functions, code a small program to test them out.

When you execute your program it should look like this:

```python
>>> python sign_up.py

Provide an email address: luis.fernando@gmail.org
Invalid email, provide a different one: 1luis@uoregon.edu
Invalid email, provide a different one: lguzman@uoregon.edu
Input your password: oregonducks
Invalid password, provide a different one: oregonducks1
Invalid password, provide a different one: oregonducks#1
Sign up successful
```

Submit a file named `"sign_up.py"` to Canvas with your code.
