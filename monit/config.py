from dotenv import load_dotenv
import os
import json

load_dotenv()

# Code info
project = os.getenv('PROJECT')
company = os.getenv('COMPANY')
location = os.getenv('LOCATION')
dev = os.getenv('DEV')

# Database info
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
database = os.getenv('DB_DATABASE')
