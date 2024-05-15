from dotenv import load_dotenv
import os
import json
import inspect

calling_script_dir = os.path.dirname(os.path.abspath(inspect.stack()[1].filename))
env_path = os.path.join(calling_script_dir, '.monit')
load_dotenv(dotenv_path=env_path)

# Code info
project = os.getenv('PROJECT')
company = os.getenv('COMPANY')
dev = os.getenv('DEV')

# Database info
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
database = os.getenv('DB_DATABASE')

db_url = f'mysql+pymysql://{user}:{password}@{host}/{database}'

# Email info
email = os.getenv('EMAIL')
email_password = os.getenv('EMAIL_PASSWORD')

if not project or not company or not dev:
    raise Exception("Por favor, as informações do código não podem ficar em branco.")

if not user or not password or not host or not database:
    raise Exception("Por favor, as informações do banco de dados não podem ficar em branco.")
