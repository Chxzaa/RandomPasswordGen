import string
import random 
from check_pass_strength import calculate_pass_strength

def main():
    length = int(input("Enter length of password:"))
    letters = string.ascii_letters + string.digits + string.punctuation
    gen_password = "".join(random.choice(letters) for i in range(length))
    calculate_pass_strength(gen_password)




main()