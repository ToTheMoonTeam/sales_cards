from web.orm.schemas.base import Base, engine, session_manager
from web.orm.schemas.sales_cards import User, SalesCard

with session_manager() as session:
    Base.metadata.create_all(bind=engine, tables=[User.__table__, SalesCard.__table__])
