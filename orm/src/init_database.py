
from orm.schemas.base import Base, engine, session_manager
from orm.schemas.sales_cards import User, SalesCard

Base.metadata.drop_all(bind=engine, tables=[User.__table__, SalesCard.__table__])
with session_manager() as session:
    Base.metadata.create_all(bind=engine, tables=[User.__table__, SalesCard.__table__])
