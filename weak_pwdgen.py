import random

# Define the lists
years = ["2018", "2019", "2020", "2021", "2022", "2023", "2023", "2024", "2025", "18", "19", "20", "21", "22", "23", "24", "25"]
seasons = ["Fall", "Winter", "Spring", "Summer"]
special = '!@$#&*'
common_pattern = ["Password", "Welcome"]
names = ["katie", "michaela", "ryan", "nick", "alex", "nicole", "lauren", "ralph", "olivia", "danielle", "xavier", "jake", "zyan", "william", "sam", "malachi", "emily", "chris", "jerry", "jason", "rob", "tom", "claire", "felix", "garry", "harry", "lincoln", "lucas", "lucy", "yasmin", "pierce", "bob", "umar"]


# first combination is with (names, years)
# second combination is with (common_pattern, years)
# third combination is with (seasons, years)

def combine_one_element_from_two_specific_lists(list1, list2):
    
    # Select one random element from each selected list
    element_1 = random.choice(list1)
    element_2 = random.choice(list2)
    
    # Combine the two elements into a single string
    return element_1 + element_2


def first_char_to_uppercase(s):
    """
    Returns a new string with the first character converted to uppercase.
    If the string is empty, returns an empty string.
    """
    if not s:
        return ""
    # Converts the first character to uppercase and concatenates it with the rest of the string
    return s[0].upper() + s[1:]

def first_char_to_lowercase(s):
    """
    Returns a new string with the first character converted to lowercase.
    If the string is empty, returns an empty string.
    """
    if not s:
        return ""
    # Converts the first character to lowercase and concatenates it with the rest of the string
    return s[0].lower() + s[1:]

run = True
which_combo = random.choice([1, 2, 3]) # Set the variable randomly anywhere between 1 through 3 to hold which combination.
special_nospecial = random.choice([True, False]) # Randomly decide whether to include a special character or not in the password.

while run:
    
    if which_combo == 1:
        pwd = combine_one_element_from_two_specific_lists(names, years)
    elif which_combo == 2:
        pwd = combine_one_element_from_two_specific_lists(common_pattern, years)
    elif which_combo == 3:
        pwd = combine_one_element_from_two_specific_lists(seasons, years)
    
    if special_nospecial == True:
        num_elements = random.choice([1, 2]) # Randomly choose to add either 1 or 2 special characters.
        pwd += ''.join(random.sample(special, k=num_elements))

    run = False # to exit the loop

'''
If true, make first letter uppercase.
If false, make first letter lowercase.
'''
upper_lower = random.choice([True, False]) # Randomly decide whether to change case of first letter.
active = True
while active:
    if upper_lower == True:
        pwd = first_char_to_uppercase(pwd)
    else:
        pwd = first_char_to_lowercase(pwd)
    
    active = False # to exit the loop

print(pwd)