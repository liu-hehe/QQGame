import model
from model.model_name import ForageWar


@model.RequestSend(cmd=ForageWar.cmd, subtype=ForageWar.subtype)
def forage_war():
    """掠夺/领取奖励"""
    return


if __name__ == '__main__':
    forage_war()
