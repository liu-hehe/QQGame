import model
from model.model_name import TenLottery


@model.RequestSend(cmd=TenLottery.cmd, op=TenLottery.op, type=TenLottery.type_high)
def ten_lottery_high():
    """邪神秘宝/领取高级秘宝"""
    return


@model.RequestSend(cmd=TenLottery.cmd, op=TenLottery.op, type=TenLottery.type_best)
def ten_lottery_best():
    """邪神秘宝/领取极品秘宝"""
    return


if __name__ == '__main__':
    ten_lottery_high()
    ten_lottery_best()
