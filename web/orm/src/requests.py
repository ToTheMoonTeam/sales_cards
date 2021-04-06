import logging

from sqlalchemy import func

from web.orm.schemas.base import session_manager
from web.orm.schemas.sales_cards import User, SalesCard

logger = logging.getLogger(__name__)


def get_cards_by_user(user_id):
    with session_manager() as session:
        try:
            sales_cards = session.query(SalesCard).filter_by(user_id=user_id).all()
            return sales_cards

        except Exception as e:
            logger.error(e)
            raise Exception("failed to get cards by user on database side")


def add_sales_card(params):
    """
        :param params: {"id": int, # can be generate if not provided
                        "company_name": string,
                        "sale": datetime,
                    }
        :return: id of registered card
    """
    with session_manager() as session:
        if "id" not in params:
            max_id = session.query(func.max(SalesCard.id)).one()[0]
            if max_id is None:
                generated_id = 1
            else:
                generated_id = str(max_id[0] + 1)

        else:
            generated_id = params["id"]
            if len(session.query(SalesCard).filter_by(id=generated_id).all()) > 0:
                raise Exception("id already in use. Try to auto-generate or choose another id")
        card = SalesCard(id=generated_id,
                         company_name=params["company_name"],
                         sale=params["sale"]
                         )
        session.add(card)
        session.flush()
        id = card.id

        session.commit()

    return id


# TODO: rewrite on args, kwargs
def add_user(params):
    """
    :param params: {"phone_number": int,
                    "name": string,
                    "birthday": datetime,
                    "work_quality": int,
                    "shipping_quality": int
                }
    :return: id of registred user
    """
    with session_manager() as session:

        test_user = User(phone_number=params["phone_number"],
                         name=params["name"],
                         birthday=params["birthday"],
                         work_quality=params["work_quality"],
                         shipping_quality=params["shipping_quality"]
                         )
        session.add(test_user)
        session.flush()
        id = test_user.id

        session.commit()

    return id


def get_user_by_id(id):
    with session_manager() as session:
        users = session.query(User).filter_by(id=id).all()
        if len(users) > 1:
            raise Exception("multple users with same id")
        if len(users) < 1:
            raise Exception("not user with id found")
    return users[0].to_dict()


def get_card_by_id(id):
    with session_manager() as session:
        cards = session.query(SalesCard).filter_by(id=id).all()
        if len(cards) > 1:
            raise Exception("multple cards with same id")
        if len(cards) < 1:
            raise Exception("not cards with id found")
    return cards[0].to_dict()


def get_all_users_data():
    with session_manager() as session:
        users = session.query(User).all()
        users_data = {}
        for item in users:
            cards = get_cards_by_user(item.id)
            users_data[item.id] = item.to_dict()
            users_data[item.id]["cards"] = [x.to_dict() for x in cards]

    return users_data


def get_all_cards_data():
    with session_manager() as session:
        cards = session.query(SalesCard).all()
        cards_data = {}
        for item in cards:
            cards_data[item.id] = item.to_dict()
    return cards_data


def remove_user_by_id(id):
    with session_manager() as session:
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


def link_sales_card_to_user(params):
    with session_manager() as session:
        user_id = params["user_id"]
        card_id = params["card_id"]

        user = session.query(User).filter_by(id=user_id).all()
        card = session.query(SalesCard).filter_by(id=card_id).all()
        assert len(user) == 1 and len(card) == 1
        user[0].sales_cards.append(card[0])
        session.commit()

