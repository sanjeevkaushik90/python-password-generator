import string
import random

print("=== Password Generator ===")

try:
    pass_length = int(input("Enter password length: "))

except ValueError:
    print("Invalid Input")


else:
    if pass_length <= 0:
        print("Invalid length")

    else:
        characters = (
            string.ascii_letters
            + string.digits
            + "!@#$%^&*"
        )

        list1 = []

        while len(list1) < pass_length:
            random_gen = random.choice(characters)
            list1.append(random_gen)

        joined = ''.join(list1)

        print("Generated password:", joined)