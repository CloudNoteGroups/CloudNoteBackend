from flask import jsonify
class ResponseCode:
    CODE_SUCCESS = 200
    CODE_NO_PARAM = 400  # 参数错误
    CODE_NOT_LOGIN = 401  # 未认证
    CODE_NOTFOUND = 404  # 资源不存在
    CODE_SERVER_ERROE = 500  # 服务器错误
    msg = {
        CODE_SUCCESS: "success",
        CODE_NO_PARAM: "params error",
        CODE_NOT_LOGIN: "not auth",
        CODE_NOTFOUND: "source not found",
        CODE_SERVER_ERROE: "sorry,server is error"
    }

def response(data=None, message=ResponseCode.msg[ResponseCode.CODE_SUCCESS],
                      code=ResponseCode.CODE_SUCCESS):
    return jsonify({
        'message': message,
        'code': code,
        'data': data
    })