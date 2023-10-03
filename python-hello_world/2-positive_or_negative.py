import random

# Assign a random signed number to the variable number
number = random.randint(-10, 10)

# Output the number and its positivity/negativity
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
