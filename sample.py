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

    num = 0
    for _ in range(3):
        num += 1

    monit.msg(f"Total count in for loop: {num}") # whatsapp

    monit.end()


if __name__ == "__main__":
    main()
