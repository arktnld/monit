# sample.py

from monit.core import Monitor as monit
from time import sleep

def main():

    try:
        sleep(5)
        raise ValueError("This is a sample error.")

    except Exception as e:
        print("Erro: Ocorreu um erro inesperado.")
        monit.notify_and_exit(e)


if __name__ == "__main__":
    main()
