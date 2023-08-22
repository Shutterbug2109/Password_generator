import random
import string


def password_gen(min_length, number = True, special_char = True):
    
    letters = string.ascii_letters
    digits = string.digits
    special_character = string.punctuation

    characters = letters 

    if number:
        characters += digits
    if special_char:
        characters += special_character

    password = ""
    meet_criteria = False
    has_number = False
    has_SpecialChar = False

    while not meet_criteria or len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special_character:
            has_SpecialChar = True
        
        meet_criteria = True
        if number:
            meet_criteria = has_number
        if special_char:
            meet_criteria = meet_criteria and  has_SpecialChar
    
    return password