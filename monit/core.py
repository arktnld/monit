from datetime import datetime
import sys
import os

from monit import config
from monit import func
from monit.database import Database, Table
from monit.verify_env import verify_env

# Ensure .env is loaded
verify_env()

# Get the initial time
INIT_TIME = datetime.now()

class Monitor:
    # TYPE = list()
    ERROR = list()

    @staticmethod
    def register(error=None):
        table = func.build_table(error, Table(), INIT_TIME)
        Database.insert(table)

    @staticmethod
    def end():
        Monitor().register(None)

    @staticmethod
    def notify(error=None):
        Monitor().register(error)

    @staticmethod
    def notify_and_exit(error=None):
        Monitor().register(error)
        sys.exit(1)
