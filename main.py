import requests
import json
import random
import string

with open('names.json', 'r') as file:
    names = json.load(file)

# URL for registration
registration_url = 'http://localhost/test/reg.php'
try:
    num_credentials = int(input("Enter the number of credentials to create: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit(1)

# Create credentials in a loop
for _ in range(num_credentials):
    random_name = random.choice(names)
    random_numbers = ''.join(random.choices(string.digits, k=3))
    username = f'{random_name}{random_numbers}'
    # Generate a random email ending
    email_endings = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
    random_email_ending = random.choice(email_endings)
    # Create the email address
    email = f'{username}@{random_email_ending}'

    passno = ''.join(random.choices(string.digits, k=6))
    password = f'{random_name}{passno}'


    # Data for registration
    data = {
        'username': email,  # Use email as the username
        'password': password,
        'submit': 'submit',
    }
    response = requests.post(registration_url, data=data)
    print(f"Created user: {email}, Response Status Code: {response.status_code}")
