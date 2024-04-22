import time
import sys
import os

from monit import config
from monit import func
from monit.database import Database, DataManager, MonitInit, MonitErr, MonitEnd

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

        self.init_time = time.perf_counter()
        self.db_manager = DatabaseManager(DB_URL)
        self.initial_register()

    def initial_register(self):
        table = func.build_table(None, None, MonitInit(), None)
        self.id_init = self.db_manager.insert_data(table)

    def register(self, table, type=None, err=None):
        table.id_init = self.id_init  # put the row id of the initial register
        table = func.build_table(type, err, table, self.init_time)
        self.db_manager.insert_data(table)

    def end(self):
        table = MonitEnd()
        self.register(table)
        self.db_manager.close()

    def notify(self, type=None, error=None):
        table = MonitErr()
        self.register(table, type, error)

    def notify_and_exit(self, type=None, error=None):
        self.notify(type, error)
        self.db_manager.close()
        sys.exit(1)
