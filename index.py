import os
from dotenv import load_dotenv

load_dotenv('.env.pro')

user_name = os.getenv('USER_NAME')
api_key = os.getenv('API_KEY')
email = os.getenv('EMAIL')
database = os.getenv('DATABASE_URL')

print(f'USER NAME: {user_name}')
print(f'API KEY: {api_key}')
print(f'EMAIL: {email}')
print(f'DATABASE URL: {database}')


