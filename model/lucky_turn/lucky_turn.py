import model
from model.model_name import LuckyTurn
from model.model_name import Page


@model.RequestSend(cmd=Page.cmd)
def page_list():
    """主页活动列表"""
    return


@model.RequestSend(cmd=LuckyTurn.cmd, subtype=LuckyTurn.subtype, op=LuckyTurn.op)
def lucky_turn():
    """幸运转盘"""
    return


if __name__ == '__main__':
    response = page_list().raw_rsp.text
    if LuckyTurn.lucky_turn in response:
        lucky_turn()
