from datetime import datetime
import sys
import os

from monit import config
from monit import func
from monit.database import Database, DataManager, Table

DB_URL = f'mysql+pymysql://{config.user}:{config.password}@{config.host}/{config.database}'

class DatabaseManager:
    def __init__(self, db_url):
        self.db = Database(db_url)
        self.data_manager = DataManager(self.db)

    def insert_data(self, data):
        id = self.data_manager.insert(data)
        return id

    def close(self):
        self.data_manager.close()


class Monitor:
    def __init__(self):
        if not os.path.exists('.env'):
                raise FileNotFoundError("Arquivo .env não encontrado. Por favor, crie um arquivo .env com as configurações necessárias.")

        self.init_time = datetime.now()
        self.db_manager = DatabaseManager(DB_URL)

        self.type = ""
        self.error = ""

    def register(self, type=None, err=None):
        table = func.build_table(type, err, Table(), self.init_time)
        self.db_manager.insert_data(table)

    def end(self):
        self.register(self.type, self.error)
        self.db_manager.close()

    def notify(self, type=None, error=None):
        self.type = type
        self.error = error
        # self.register(type, error)

    def notify_and_exit(self, type=None, error=None):
        self.register(type, error)
        self.db_manager.close()
        sys.exit(1)
