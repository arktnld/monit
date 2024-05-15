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
    TYPE = list()
    ERROR = list()

    def register(self, type=None, error=None):
        table = func.build_table(type, error, Table(), INIT_TIME)
        Database.insert(table)

    def end(self):
        # type = ', '.join(self.TYPE)
        # error = ', '.join(self.ERROR)
        self.register(None, None)

    def notify(self, type=None, error=None):
        self.TYPE.append(type)
        self.ERROR.append(error)

    @staticmethod
    def notify_and_exit(type=None, error=None):
        Monitor().register(type, error)
        sys.exit(1)
