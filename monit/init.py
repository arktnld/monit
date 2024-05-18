# monit.py

from dotenv import load_dotenv
from dotenv import set_key


def create_template():
    env_path = '.monit'

    set_key(env_path, 'PROJECT', "project_name")
    set_key(env_path, 'COMPANY', "company_name")
    set_key(env_path, 'DEV', "coder")
    set_key(env_path, 'LOCATION', "location_name")
    set_key(env_path, 'HANDLER_URL', "https://example.com")
    set_key(env_path, 'PHONE', "")

    load_dotenv(dotenv_path=env_path)
