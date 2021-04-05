from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager


engine = create_engine('postgresql://admin:admin@localhost:5432/sales_cards')
Session = sessionmaker(bind=engine)

Base = declarative_base()


@contextmanager
def session_manager():
    session = Session()
    try:
        yield session
    finally:
        session.close()
