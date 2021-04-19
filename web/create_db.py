from orm.schemas.base import Base, engine
from orm.schemas.sales_cards import User, SalesCard

def init_db():
    Base.metadata.create_all(bind=engine, tables=[User.__table__, SalesCard.__table__])
