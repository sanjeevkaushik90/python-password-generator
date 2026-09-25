import string
import random

print("=== Password Generator ===")

pass_length = int(input("Enter password length: "))

characters = (
    string.ascii_letters
    + string.digits
    + "!@#$%^&*"
)

list1 = []

while len(list1) < pass_length:
    random_gen = random.choice(characters)
    list1.append(random_gen)
    # list1+=(random_gen)

    joined = ''.join(list1)

print(joined)