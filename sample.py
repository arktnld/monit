#
# sample.py
from time import sleep

from monit.core import Monitor as monit
from monit.logger import Logger
from monit.log2file import Log2File

def main():

    Log2File() # Salva todo o log em um arquivo
    log = Logger()

    try:
        log.info("Hello, World!")

        sleep(2)
        raise ValueError("This is a sample error.")

    except Exception as e:
        monit.notify(e)

    try:
        sleep(2)
        raise ValueError("This is another a sample error.")

    except Exception as e:
        monit.notify(e, "Custom message") # Mensagem personalizada

    num = 0
    for _ in range(3):
        num += 1
    monit.msg(f"Total count in for loop: {num}")

    monit.end()


if __name__ == "__main__":
    main()


