from flask import jsonify


def format_resp(code=0, msg='', data=None):
    """
    格式化输出
    :param code:
    :param msg:
    :param data:
    :return:
    """
    ret_dict = {
        'code': code,
        'msg': msg,
        'data': {}
    }
    if data:
        ret_dict['data'] = data
    return jsonify(ret_dict)
