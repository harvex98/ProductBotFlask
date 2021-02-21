from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///C:\\Users\\Klugman\\Documents\\pyDev\\ProductEntry\\entrybot\\database\\sqlite3\\entrybot.db', convert_unicode=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()

def init_db():
    import entrybot.database.models
    Base.metadata.create_all(bind=engine)
