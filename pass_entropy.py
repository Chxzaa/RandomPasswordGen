import string
import math

def calculate_entropy(password):
    charset_size = 0
    if any(char in string.ascii_lowercase for char in password):
        charset_size += 26
    if any(char in string.ascii_uppercase for char in password):
        charset_size += 26
    if any(char in string.digits for char in password):
        charset_size += 10
    if any(char in string.punctuation for char in password):
        charset_size += len(string.punctuation)
    if any(char.isspace() for char in password):
        charset_size += 1

    return len(password) * math.log2(charset_size) if charset_size else 0
