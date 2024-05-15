# sample.py
import time

from pymonit.core import Monitor
from pymonit.error import SetupError, HTTPError
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
        monit.notify(SetupError, e)

    try:
        # Your code that might raise exceptions
        time.sleep(2)
        raise ValueError("This is another a sample error.")

    except Exception as e:
        print("Erro: Ocorreu um erro inesperado.")
        monit.notify(HTTPError, e)

    monit.end()


if __name__ == "__main__":
    main()

