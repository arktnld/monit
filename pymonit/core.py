from datetime import datetime
import sys
import os

from pymonit import config
from pymonit import func
from pymonit.database import Database, Table
from pymonit.verify_env import verify_env

# Ensure .env is loaded
verify_env()

# Get the initial time
INIT_TIME = datetime.now()

class Monitor:
    TYPE = list()
    ERROR = list()

    @staticmethod
    def register(type=None, error=None):
        table = func.build_table(type, error, Table(), INIT_TIME)
        Database.insert(table)

    @staticmethod
    def end():
        Monitor().register(None, None)

    @staticmethod
    def notify(type=None, error=None):
        Monitor().register(type, error)

    @staticmethod
    def notify_and_exit(type=None, error=None):
        Monitor().register(type, error)
        sys.exit(1)
