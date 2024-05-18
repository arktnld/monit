from dotenv import load_dotenv
import os
import inspect

from monit.init import create_template

calling_script_dir = os.path.dirname(os.path.abspath(inspect.stack()[1].filename))
env_path = os.path.join(calling_script_dir, '.monit')
load_dotenv(dotenv_path=env_path)

if not os.path.isfile(env_path):
    create_template()
    raise Exception("Arquivo de configuraçao '.monit' não existe")

project = os.getenv('PROJECT')
company = os.getenv('COMPANY')
dev = os.getenv('DEV')
location = os.getenv('LOCATION')
handler_url = os.getenv('HANDLER_URL')
phone = os.getenv('PHONE')

if not project or not company or not dev or not location or not handler_url:
    empty_vars = [name for name, value in [("project", project), ("company", company), ("dev", dev), ("location", location), ("handler_url", handler_url)] if not value]
    error_msg = f"Informações do código não foram preenchidas no arquivo de configuração: {', '.join(empty_vars)}"
    raise Exception(error_msg)
