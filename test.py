import requests
import random
import string

registration_url = 'http://localhost/test/reg.php'

email = f'tom'
password = f'pass123'

data = {
    'username': email,
    'password': password,
    'submit': 'submit',
}
response = requests.post(registration_url, data=data)
print(f"Created user: {email}, Response Status Code: {response.status_code}")
