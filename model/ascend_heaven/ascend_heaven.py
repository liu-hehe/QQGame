import model
from model.model_name import AscendHeaven
from public_common.get_cookie import GetCookie

config_sections = GetCookie().get_cookie().sections()  # 获取config的key
config_options_num = GetCookie.get_cookie().options(config_sections[0]) if config_sections else None  # 获取config的第一个key的所有value
ascend_heaven_sign_up = GetCookie.get_cookie().get(config_sections[0], config_options_num[2]) if config_sections and config_options_num else None  # 获取config的第一个key的第三个value


@model.RequestSend(cmd=AscendHeaven.cmd, op=AscendHeaven.op_view_sign_up, type=ascend_heaven_sign_up)
def ascend_heaven_view_sign_up_rank():
    """飞升大作战/是否报名"""
    return


@model.RequestSend(cmd=AscendHeaven.cmd, op=AscendHeaven.op_sign_up, type=ascend_heaven_sign_up)
def ascend_heaven_sign_up_rank():
    """飞升大作战/确认报名"""
    return


if __name__ == '__main__':
    ascend_heaven_view_sign_up_rank()
    ascend_heaven_sign_up_rank()
