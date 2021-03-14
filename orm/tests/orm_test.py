from pprint import pprint

from orm.schemas.base import Base, engine, Session
from orm.schemas.sales_cards import User, SalesCard


def create_all():
    Base.metadata.create_all(engine)


def fill_user():
    session = Session()

    test_user = User("+79811207498", "vasily")
    session.add(test_user)

    session.commit()
    session.close()


def fill_card():
    session = Session()
    for c_id in [1, 2, 3]:
        test_card = SalesCard(id=c_id, company_name=f"testCompany{c_id}", sale=0.5)
        test_card.user_id = 1
        session.add(test_card)
        session.commit()
    session.close()


def get_all():
    session = Session()
    users = session.query(User).filter_by(id=0).all()
    sales_cards = session.query(SalesCard).all()
    session.close()
    return users, sales_cards


def get_cards_linked_to_user():
    session = Session()
    sales_cards = session.query(SalesCard).filter_by(user_id=1).all()
    return sales_cards


def test_orm():
    create_all()  # create_all indeed creates only tables that do not exist
    fill_user()
    fill_card()
    assert len(get_all()) > 0
    pprint([x.to_dict() for x in get_cards_linked_to_user()])
    assert len(get_cards_linked_to_user()) == 3


# WARNING : will clear all database
# TODO: create database for tests
#Base.metadata.drop_all(bind=engine, tables=[User.__table__, SalesCard.__table__])

test_orm()
