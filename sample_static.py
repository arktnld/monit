# sample.py

#
#  IMPORTANTE: importar OS e entrar na pasta atual é obrigatório no inicio do arquivo
#
import os

script_path = os.path.abspath(__file__)
os.chdir(os.path.dirname(script_path))
import time

from monit.core import Monitor as monit
from monit.error import SetupError

def main():

    try:
        time.sleep(5)
        raise ValueError("This is a sample error.")

    except Exception as e:
        print("Erro: Ocorreu um erro inesperado.")
        monit.notify_and_exit(e)


if __name__ == "__main__":
    main()
