import flask
from flask import request, jsonify
import logging

from sqlalchemy.exc import ProgrammingError

from app.src.common.common import no_request_argument_provided_error, wrong_type_argument_provided
from orm.src.requests import get_cards_by_user, add_user, get_user_by_id, get_all_users_data, remove_user_by_id, \
    add_sales_card, get_card_by_id, link_sales_card_to_user, get_all_cards_data

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/get_users_cards', methods=['GET'])
def get_users_card():
    request_key = "user_id"
    if request_key not in request.args:
        return no_request_argument_provided_error(request_key)
    try:
        cards = get_cards_by_user(request.args[request_key])
    except Exception as e:
        logger.error(e)
        resp = jsonify({"body": str(e)})
        resp.status_code = 422
        return resp
    resp = jsonify({
        "body": {
            "cards": {i: data.to_dict() for i, data in zip(range(len(cards)), cards)}
        }})
    resp.status_code = 200
    return resp


@app.route('/register', methods=['POST'])
def register():
    request_keys = ["phone_number", "name", "birthday", "work_quality", "shipping_quality"]
    for item in request_keys:
        if item not in request.args:
            return no_request_argument_provided_error(item)
    try:
        registred_id = add_user(request.args)
    except Exception as e:
        logger.error(e)
        resp = jsonify({"body": str(e)})
        resp.status_code = 422
        return resp
    resp = jsonify({
        "body": {
            "usr": get_user_by_id(registred_id),
            "msg": "registered"
        }})
    resp.status_code = 200
    return resp


@app.route('/register_card', methods=['POST'])
def register_card():
    request_keys = ["company_name", "sale"]
    for item in request_keys:
        if item not in request.args:
            return no_request_argument_provided_error(item)
    try:
        registred_id = add_sales_card(request.args)
    except Exception as e:
        logger.error(e)
        resp = jsonify({"body": str(e)})
        resp.status_code = 422
        return resp
    resp = jsonify({
        "body": {
            "card": get_card_by_id(registred_id),
            "msg": "registered"
        }})
    resp.status_code = 200
    return resp


@app.route('/get_all_users', methods=['get'])
def get_all_users():
    try:
        users_cards = get_all_users_data()
    except ProgrammingError as e:
        logger.error(e)
        resp = jsonify({"body": "Empty database"})
        resp.status_code = 422
        return resp
    except Exception as e:
        logger.error(e)
        resp = jsonify({"body": str(e)})
        resp.status_code = 422
        return resp
    resp = jsonify({
        "body": {
            "all_users": users_cards
        }})
    resp.status_code = 200
    return resp


@app.route('/get_all_cards', methods=['get'])
def get_all_cards():
    try:
        cards_data = get_all_cards_data()
    except ProgrammingError as e:
        logger.error(e)
        resp = jsonify({"body": "Empty database"})
        resp.status_code = 422
        return resp

    except Exception as e:
        logger.error(e)
        resp = jsonify({"body": str(e)})
        resp.status_code = 422
        return resp
    resp = jsonify({
        "body": {
            "all_cards": cards_data
        }})
    resp.status_code = 200
    return resp


@app.route('/remove_user', methods=['POST'])
def remove_user():
    request_keys = ["id"]
    for item in request_keys:
        if item not in request.args:
            return no_request_argument_provided_error(item)

    try:
        remove_user_by_id(request.args[request_keys[0]])
    except ProgrammingError as e:
        logger.error(e)
        resp = jsonify({"body": "Empty database"})
        resp.status_code = 422
        return resp
    except Exception as e:
        logger.error(e)
        resp = jsonify({"body": str(e)})
        resp.status_code = 422
        return resp
    resp = jsonify({
        "body": {
            "msg": f"removed user{request.args[request_keys[0]]}"
        }})
    resp.status_code = 200
    return resp


@app.route('/link_card', methods=['POST'])
def link_card():
    request_keys = ["user_id", "card_id"]
    for item in request_keys:
        if item not in request.args:
            return no_request_argument_provided_error(item)

    try:
        link_sales_card_to_user(request.args)
    except ProgrammingError as e:
        logger.error(e)
        resp = jsonify({"body": "Empty database"})
        resp.status_code = 422
        return resp
    except Exception as e:
        logger.error(e)
        resp = jsonify({"body": str(e)})
        resp.status_code = 422
        return resp
    resp = jsonify({
        "body": {
            "card": get_card_by_id(request.args["card_id"]),
            "user": get_user_by_id(request.args["user_id"]),
            "msg": "linked"
        }})
    resp.status_code = 200
    return resp


app.run()
