import model
from model.model_name import LuanDou


@model.RequestSend(cmd=LuanDou.cmd, op=LuanDou.op)
def luan_dou_reward():
    """全民乱斗奖励领取"""
    return


if __name__ == '__main__':
    for i in range(15, 20):
        luan_dou_reward(id=i)