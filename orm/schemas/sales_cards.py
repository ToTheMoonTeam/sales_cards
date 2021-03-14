from sqlalchemy import Column, Integer, ForeignKey, String, Float
from orm.schemas.base import Base


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    phone_number = Column(String, nullable=False)

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone_number": self.phone_number
        }


class SalesCard(Base):
    __tablename__ = 'SalesCard'

    id = Column(Integer, primary_key=True)
    company_name = Column(String)
    sale = Column(Float)
    user_id = Column(Integer, ForeignKey('User.id', onupdate="SET NULL", ondelete="SET NULL"))

    def __init__(self, id, company_name, sale):
        self.id = id
        self.company_name = company_name
        self.sale = sale

    def to_dict(self):

        return {
            "id": self.id,
            "company_name": self.company_name,
            "sale": self.sale,
        }
