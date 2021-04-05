from sqlalchemy import Column, Integer, ForeignKey, String, Float, DateTime
from sqlalchemy.orm import relationship
from sales_cards.orm.schemas.base import Base


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    birthday = Column(DateTime)
    work_quality = Column(Integer)
    shipping_quality = Column(Integer)
    phone_number = Column(String, nullable=False)
    sales_cards = relationship('SalesCard')

    def __init__(self, name, phone_number, birthday, work_quality, shipping_quality):
        self.name = name
        self.phone_number = phone_number
        self.birthday = birthday
        self.work_quality = work_quality
        self.shipping_quality = shipping_quality
        self.schema = self.__tablename__

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone_number": self.phone_number,
            "birthday": self.birthday,
            "work_quality": self.work_quality,
            "shipping_quality": self.shipping_quality
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
        self.schema = self.__tablename__

    def to_dict(self):
        return {
            "id": self.id,
            "company_name": self.company_name,
            "sale": self.sale,
        }
