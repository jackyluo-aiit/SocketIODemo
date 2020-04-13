def resultVo(data, status):
    dict = {}
    dict["data"] = data
    dict["status"] = status
    return dict


def statusVo(message, status):
    dict = {}
    dict["message"] = message
    dict["status"] = status
    return dict


def args_verification(*args):
    for each in args:
        if each is None:
            return False
    return True
