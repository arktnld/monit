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

        sleep(10)
        raise ValueError("Isso é um teste de erro 2.")

    except Exception as e:
        monit.notify(e)

    monit.msg("O Script terminou com sucesso.") # whatsapp

    monit.end() # manda sinal de fim sem erros


if __name__ == "__main__":
    main()
