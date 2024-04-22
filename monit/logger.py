import logging
import os
from logging.handlers import TimedRotatingFileHandler
import sys
# import io


class LoggingConfigurator:
    # Classe responsável por configurar o logger.

    @staticmethod
    def get_logger(log_level):
        logger = logging.getLogger()
        if not logger.handlers:  # Configure o logger apenas se os manipuladores ainda não estiverem configurados
            logger.setLevel(log_level)

            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(LoggingConfigurator.get_formatter())
            logger.addHandler(console_handler)

            # file_handler = TimedRotatingFileHandler(LoggingConfigurator.get_log_file(), when='midnight', encoding='utf-8')
            # file_handler.setFormatter(LoggingConfigurator.get_formatter())
            # logger.addHandler(file_handler)

            logger.propagate = False
        return logger

    @staticmethod
    def get_formatter():
        # return logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s] %(message)s")
        return logging.Formatter(
            fmt="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

    @staticmethod
    def get_log_file():
        log_dir = 'logs'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        return os.path.join(os.getcwd(), log_dir, os.path.splitext(os.path.basename(__file__))[0] + '.log')


class Logger:

    @staticmethod
    def debug(message):
        logger = LoggingConfigurator.get_logger(logging.DEBUG)
        logger.debug(message)

    @staticmethod
    def info(message):
        logger = LoggingConfigurator.get_logger(logging.INFO)
        logger.info(message)

    @staticmethod
    def warning(message):
        logger = LoggingConfigurator.get_logger(logging.WARNING)
        logger.warning(message)

    @staticmethod
    def error(message):
        logger = LoggingConfigurator.get_logger(logging.ERROR)
        logger.error(message)

    @staticmethod
    def critical(message):
        logger = LoggingConfigurator.get_logger(logging.CRITICAL)
        logger.critical(message)


# Exemplo de uso:
if __name__ == "__main__":
    log = Logger()

    log.debug('Mensagem de Debug')
    log.info('Mensagem de Informação')
    log.warning('Mensagem de Aviso')
    log.error('Mensagem de Erro')
    log.critical('Mensagem Crítica')

    print("Esta é uma saída padrão.")
    raise ValueError("Esta é uma exceção para testar a saída de erro.")

