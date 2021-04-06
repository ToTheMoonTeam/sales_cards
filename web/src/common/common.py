from flask import jsonify
import logging
import xlsxwriter

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


def generate_excele(users):
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('AllUsers.xlsx')
    worksheet = workbook.add_worksheet()

    datetime_format = workbook.add_format({'num_format': 'dd/mm/yy'})
    header = ["id",
              "name",
              "phone_number",
              "birthday",
              "work_quality",
              "shipping_quality"]
    for item in header:
        worksheet.write(0, header.index(item), item)
    row = 1
    for item in users:
        for col in range(len(item)):
            if col == 3:
                worksheet.write(row, col, item[col], datetime_format)
            else:
                worksheet.write(row, col, item[col])
        row += 1
    workbook.close()
