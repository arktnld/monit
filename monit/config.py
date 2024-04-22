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

# Email info
email = os.getenv('EMAIL')
email_password = os.getenv('EMAIL_PASSWORD')

if not project or not company or not location or not dev:
    raise Exception("Por favor, as informações do código não podem ficar em branco.")

if not user or not password or not host or not database:
    raise Exception("Por favor, as informações do banco de dados não podem ficar em branco.")
