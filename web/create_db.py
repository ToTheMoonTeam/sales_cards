from orm.schemas.base import Base, session_manager, engine
from orm.schemas.sales_cards import User, SalesCard, SalesCardExemplar

with session_manager() as session:
    Base.metadata.create_all(bind=engine, tables=[User.__table__, SalesCard.__table__, SalesCardExemplar.__table__])
