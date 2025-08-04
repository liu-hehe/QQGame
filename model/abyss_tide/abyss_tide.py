import model
import re
from model.model_name import AbyssTide
from public_common.get_cookie import GetCookie
from public_common.request import HTTPRequester

config_sections = GetCookie().get_cookie().sections()  # 获取config的key
config_options_num = GetCookie.get_cookie().options(config_sections[0]) if config_sections else None# 获取config的第一个key的所有value
abyss_tide_enter_chose = GetCookie.get_cookie().get(config_sections[0], config_options_num[1]) if config_options_num else None# 获取config的第一个key的第二个value


@model.RequestSend(cmd=AbyssTide.cmd, op=AbyssTide.op_get_faction_gift)
def abyss_tide_gift():
    """深渊之潮/帮派巡礼/领取"""
    return


@model.RequestSend(re_exp=r"今日可进入副本次数：(\w+)<br", cmd=AbyssTide.cmd, op=AbyssTide.op_view_all_abyss)
def abyss_tide_times():
    """深渊之潮/深渊秘境/进入副本次数"""
    return


@model.RequestSend(cmd=AbyssTide.cmd, op=AbyssTide.op_confirm, type=AbyssTide.type_enter, id=abyss_tide_enter_chose)
def abyss_tide_enter():
    """深渊之潮/深渊秘境/是否进入"""
    return


@model.RequestSend(cmd=AbyssTide.cmd, op=AbyssTide.op_enter_abyss, id=abyss_tide_enter_chose)
def abyss_tide_enable():
    """深渊之潮/深渊秘境/进入"""
    return


@model.RequestSend(cmd=AbyssTide.cmd, op=AbyssTide.op_begin_fight)
def abyss_tide_fight():
    """深渊之潮/帮派巡礼/开始挑战"""
    return


@model.RequestSend(cmd=AbyssTide.cmd, op=AbyssTide.op_confirm, type=AbyssTide.type_settle)
def abyss_tide_settle():
    """深渊之潮/深渊秘境/是否结算副本"""
    return


@model.RequestSend(cmd=AbyssTide.cmd, op=AbyssTide.op_end_abyss)
def abyss_tide_end_abyss():
    """深渊之潮/深渊秘境/结算副本"""
    return


if __name__ == '__main__':
    abyss_tide_gift()
    times = abyss_tide_times()
    if times:
        for i in range(int(times[0])):
            abyss_tide_enter()
            abyss_tide_enable()
            for i in range(5):
                abyss_tide_fight()
            abyss_tide_settle()
            abyss_tide_end_abyss()