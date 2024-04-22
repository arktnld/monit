from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Text
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class BaseTable(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    project = Column(String(255))
    company = Column(String(255))
    dev = Column(String(255))
    date = Column(DateTime)
    cpu = Column(String(255))
    mem = Column(String(255))
    disk = Column(String(255))
    system = Column(String(255))
    ping = Column(Integer)

class MonitInit(BaseTable):
    __tablename__ = 'monit_init'

class MonitErr(BaseTable):
    __tablename__ = 'monit_err'
    id_init = Column(Integer)
    type = Column(String(255))
    error = Column(Text)
    runtime = Column(Integer)

class MonitEnd(BaseTable):
    __tablename__ = 'monit_end'
    id_init = Column(Integer)
    runtime = Column(Integer)

class Database:
    def __init__(self, url):
        self.engine = create_engine(url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

class DataManager:
    def __init__(self, db):
        self.db = db
        self.session = self.db.get_session()

    def insert(self, data):
        self.session.add(data)
        self.session.commit()
        # Após a inserção, os IDs das linhas serão atualizados nos objetos data
        # inserted_ids = [data_instance.id for data_instance in data]
        return data.id

    def close(self):
            self.session.close()

# def main():
#     db_url = 'mysql://arktnld:npndtdes@localhost/teste'
#     db = Database(db_url)
#     data_manager = DataManager(db)

#     table = Table1()

#     table.project = 'project_1'
#     table.company = 'company_1'
#     table.dev = 'dev_1'
#     table.date = datetime.now()
#     table.stderr = True
#     table.type = 'SetupError'
#     table.error = 'This is a sample error.'
#     table.runtime = 5
#     table.cpu = '2.50%'
#     table.mem = '46.00%'
#     table.disk = '49%'
#     table.system = 'Linux'
#     table.ping = 22

#     id = data_manager.insert_data(table)
#     print(id)

# if __name__ == "__main__":
#     main()
