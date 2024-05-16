from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Text
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy.orm import declarative_base
from monit import config

Base = declarative_base()

class Table(Base):
    __tablename__ = 'monit'

    id = Column(Integer, primary_key=True)
    project = Column(String(255))
    company = Column(String(255))
    dev = Column(String(255))
    # type = Column(String(255))
    stderr = Column(Boolean)
    error = Column(Text)
    runtime = Column(Integer)
    date_init = Column(DateTime)
    date_end = Column(DateTime)
    cpu = Column(String(255))
    mem = Column(String(255))
    disk = Column(String(255))
    system = Column(String(255))
    ping = Column(Integer)

class DatabaseSession:
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
        return data.id

    def close(self):
            self.session.close()

class Database:
    @staticmethod
    def insert(data):
        db = DatabaseSession(config.db_url)
        data_manager = DataManager(db)
        id = data_manager.insert(data)
        data_manager.close()
        return id
