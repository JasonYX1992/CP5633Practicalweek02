"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIALS = "!@#$%^&*()_-=+`~,./o'[]\<>?O{}|"


def main():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIALS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(len(password)) + " character password is valid: " + password)


def is_valid_password(password):
    # TODO: if length is wrong, return False

    if len(password) < MIN_LENGTH and len(password) > MAX_LENGTH:
        print("You length not enough!!")
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        # TODO: count each kind of character
        if str.islower(char):
            count_lower += 1

        if str.isupper(char):
            count_upper += 1

        if str.isdigit(char):
            count_digit += 1

        if SPECIALS.find(char) >= 0:
            count_special += 1
    pass


    # TODO: if any of the 'normal' counts are zero, return False
    if count_digit <= 0:

        return False

    elif count_lower <= 0:

        return False
    elif count_upper <= 0:

        return False

    # TODO: if special characters are required, then check the count of those and return False if it's zero
    elif count_special <= 0:

        return False
    else:

        return True


    # if we get here (without having returned False), then the password must be valid

main()








