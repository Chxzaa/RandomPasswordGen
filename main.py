import string
import random 

length = int(input("Enter length of password:"))
letters = string.ascii_letters + string.digits + string.punctuation
gen_password = "".join(random.choice(letters) for i in range(length))
print (gen_password)

