from flask import Response

ERR_INVALID_ARGUMENTS = 400
ERR_AUTH_FAILED = 401
ERR_NOT_FOUND = 404
ERR_CONFLICTION = 409
ERR_INTERNAL_SERVER = 500

MSG_OK = "OK"
MSG_ERR = "ERR"
MSG_AUTH_ERR = "AUTH_ERR"

DEBUG_ERR_REACH_END = "未匹配任何期望条件而到达函数底部"
DEBUG_ERR_ARGUMENT = "传入了错误的参数"
DEBUG_EXCEPT_SQL = "由于数据库操作时出现问题而造成的错误："
DEBUG_EXCEPT_INTERNAL = "由于内部故障而造成的错误："
DEBUG_CONDITION_NOT_MATCH = "条件不匹配"
DEBUG_CONFLICTION = "项已存在"
DEBUG_NOT_FOUND = "项未找到"


def return_to_server(
    message: str | None = MSG_OK,
    code: int = 200,
    debug: str = "",
    data: list | dict | None = None,
) -> Response:
    if debug:
        print(debug)
    return {"msg": message, "data": data}, code
