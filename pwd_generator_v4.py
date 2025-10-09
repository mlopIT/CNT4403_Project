import random
import string

# Set the minimum password length randomly anywhere between 8 through 12.
min_Length= random.randint(8,12)

# Define the characters to use in the password
letters = string.ascii_letters
digits = string.digits
special = '!@' # originally -> string.punctuation
characters = letters + digits + special
# print(letters, digits, special) '''to see what it looks like'''

# Generate the password
pwd = '' # this variable is what will store the password
last_char = None
while len(pwd) < min_Length:
    new_char = random.choice(characters)
    if new_char != last_char or len(pwd) == 0:
        pwd += new_char
        last_char = new_char
    # pwd += new_char

# Check if the password has a number and/or special character
has_number = any(c in digits for c in pwd)
has_special = any(c in special for c in pwd)

max_numbers = 2 # set the maximum number of numbers to add
current_numbers = 0 # initialize the current number of numbers to 0
while not has_number and current_numbers < max_numbers:
    pwd += random.choice(digits)
    current_numbers += 1

max_special = 2 # set the maximum number of special characters to add
current_special = 0 # initialize the current number of special characters to 0
while not has_special and current_special < max_special:
    pwd += random.choice(special)
    current_special += 1


print(pwd)

