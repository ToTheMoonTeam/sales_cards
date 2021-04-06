from flask import jsonify
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def no_request_argument_provided_error(argument):
    error_msg = f"failed: missed {argument} argument in request"
    logger.error(error_msg)
    resp = jsonify({"body": error_msg})
    resp.status_code = 400
    return resp


def wrong_type_argument_provided(argument, arg_type):
    error_msg = f"failed:  argument {argument} is wrong type: should be {arg_type}-convertable"
    logger.error(error_msg)
    resp = jsonify({"body": error_msg})
    resp.status_code = 422
    return resp


def wrong_argument_provided(argument, reason):
    error_msg = f"failed:  argument {argument} is incorrect: {reason}"
    logger.error(error_msg)
    resp = jsonify({"body": error_msg})
    resp.status_code = 422
    return resp

