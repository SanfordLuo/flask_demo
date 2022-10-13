from flask import jsonify


def format_resp(code=0, message='', data=None):
    """
    格式化输出
    :param code:
    :param message:
    :param data:
    :return:
    """
    ret_dict = {
        'code': code,
        'message': message,
        'data': {}
    }
    if data:
        ret_dict['data'] = data
    return jsonify(ret_dict)
