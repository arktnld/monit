import logging
import os
from logging.handlers import TimedRotatingFileHandler
import sys


class LoggingConfigurator:

    @staticmethod
    def get_logger(log_level):
        logger = logging.getLogger()
        if not logger.handlers:
            logger.setLevel(log_level)

            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(LoggingConfigurator.get_formatter())
            logger.addHandler(console_handler)

            logger.propagate = False
        return logger

    @staticmethod
    def get_formatter():
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
