import model
from model.model_name import DailyChest


@model.RequestSend(cmd=DailyChest.cmd, op=DailyChest.op, type=DailyChest.type_copper)
def daily_chest_copper():
    """每日宝箱/领取铜质"""
    return


@model.RequestSend(cmd=DailyChest.cmd, op=DailyChest.op, type=DailyChest.type_silver)
def daily_chest_silver():
    """每日宝箱/领取银质"""
    return


@model.RequestSend(cmd=DailyChest.cmd, op=DailyChest.op, type=DailyChest.type_gold)
def daily_chest_gold():
    """每日宝箱/领取金质"""
    return


if __name__ == '__main__':
    daily_chest_copper()
    daily_chest_silver()
    daily_chest_gold()
