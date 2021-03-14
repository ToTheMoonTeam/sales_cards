import logging

from orm.schemas.base import Base, engine, Session
from orm.schemas.sales_cards import User, SalesCard

logger = logging.getLogger(__name__)


def get_cards_by_user(user_id):
    session = Session()
    try:
        sales_cards = session.query(SalesCard).filter_by(user_id=user_id).all()
        return sales_cards

    except Exception as e:
        logger.error(e)
        raise Exception("failed to get cards by user on database side")


def add_user(phone_number, name):
    session = Session()

    test_user = User(phone_number=phone_number, name=name)
    session.add(test_user)
    session.flush()
    id = test_user.id

    session.commit()

    session.close()
    return id


def get_user_by_id(id):
    session = Session()
    users = session.query(User).filter_by(id=id).all()
    if len(users) > 1:
        raise Exception("multple users with same id")
    if len(users) < 1:
        raise Exception("not user with id found")
    session.close()
    return users[0].to_dict()


def get_all_users_data():
    session = Session()
    users = session.query(User).all()
    users_cards = {}
    for item in users:
        cards = get_cards_by_user(item.id)
        users_cards[item.id] = [x.to_dict() for x in cards]
    session.close()
    return users_cards


def remove_user_by_id(id):
    session = Session()
    to_remove_user = session.query(User).filter_by(id=id).all()
    if len(to_remove_user) > 1:
        logger.error("multiple users on same id ")
    elif len(to_remove_user) < 1:
        logger.warning("try to deletу not existed user")
    elif to_remove_user is not None:
        to_remove_user = to_remove_user[0]
        linked_cards = session.query(SalesCard).filter_by(user_id=to_remove_user.id).all()
        for item in linked_cards:
            if item is not None:
                session.delete(item)
                session.flush()
        session.delete(to_remove_user)

    session.commit()
    session.close()

