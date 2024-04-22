# sample.py
import time

from monit.core import Monitor
from monit.error import SetupError
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
        # monit.notify_and_exit(SetupError, e)

    monit.end()


if __name__ == "__main__":
    main()
