import random

# Generate a random signed number between -10000 and 10000
number = random.randint(-10000, 10000)

# Extract the last digit of the number
last_digit = abs(number) % 10

# Determine the appropriate message based on the last digit
message = f"Last digit of {number} is {last_digit} and"

if last_digit > 5:
    message += " is greater than 5"
elif last_digit == 0:
    message += " is 0"
else:
    message += " is less than 6 and not 0"

# Print the final message
print(message)
