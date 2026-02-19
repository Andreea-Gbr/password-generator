import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print("--- Secure Password Generator ---")

try:
    user_input = int(input("Enter password length: "))
    
    # Check if the number is positive
    if user_input <= 0:
        print("Error: Please enter a positive number greater than 0.")
    elif user_input > 128:
        print("Error: Password length is too long (Max 128).")
    else:
        print(f"Your new password is: {generate_password(user_input)}")

except ValueError:
    print("Error: Invalid input. Please enter a whole number (e.g., 12).")