#
# sample.py

#
#  IMPORTANTE: importar OS e entrar na pasta atual é obrigatório no inicio do arquivo,
#              para que o script seja executado corretamente em agendadores de tarefa.
#
import os

script_path = os.path.abspath(__file__)
os.chdir(os.path.dirname(script_path))

import time

from monit.core import Monitor
from monit.error import SetupError, HTTPError
# from monit.logger import Logger
# from monit.log2file import Log2File

def main():
    # Initialize the Monitor
    monit = Monitor()

    # Log2File()
    # log = Logger()

    try:
        # Your code that might raise exceptions
        time.sleep(5)
        raise ValueError("This is a sample error.")

    except Exception as e:
        print("Erro: Ocorreu um erro inesperado.")
        monit.notify(e)

    try:
        # Your code that might raise exceptions
        time.sleep(2)
        raise ValueError("This is another a sample error.")

    except Exception as e:
        print("Erro: Ocorreu um erro inesperado.")
        monit.notify(e)

    monit.end()


if __name__ == "__main__":
    main()


