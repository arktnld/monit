# sample.py
import time

from monit.core import Monitor as monit
from monit.error import SetupError

def main():

    try:
        time.sleep(5)
        raise ValueError("This is a sample error.")

    except Exception as e:
        print("Erro: Ocorreu um erro inesperado.")
        monit.notify_and_exit(SetupError, e)


if __name__ == "__main__":
    main()
