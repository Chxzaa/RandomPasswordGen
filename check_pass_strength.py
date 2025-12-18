import random
import os
import string
import math
from pass_entropy import calculate_entropy
MIN_LENGTH = 8
def calculate_pass_strength(password):

    if len(password) < MIN_LENGTH:
        print(f"Password too short! Must be {MIN_LENGTH} characters!")
        return 
    
    lower_case = 0 
    for c in password:
        if c in string.ascii_lowercase:
            lower_case += 1

    upper_case = 0 
    for c in password:
        if c in string.ascii_uppercase:
            upper_case += 1
    
    num_count = 0 
    for c in password:
        if c in string.digits:
            num_count += 1
    
    special_count = 0 
    for c in password:
        if c in string.punctuation:
            special_count += 1
    
    whitespace_count = 0 
    for c in password:
        if c.isspace():
            whitespace_count += 1

    entropy = calculate_entropy(password)



    if entropy < 28:
        remarks = "⚠️ Very Weak."
    elif entropy < 36:
        remarks = "⚠️ Weak."
    elif entropy < 60:
        remarks = "✅ Moderate."
    elif entropy < 80:
        remarks = "✅ Strong."
    else:
        remarks = "✅ Very Strong."


    print(f"Your random password is {password}")
    print("Password stats:")
    print(f"{lower_case} lowercase letters")
    print(f"{upper_case} uppercase letters")
    print(f"{num_count} digits")
    print(f"{special_count} special characters")
    print(f"{whitespace_count} whitespace characters")
    print(f"Entropy Score: {entropy:.2f} bits")
    print(f"Remarks: {remarks}\n")






    

    

    




