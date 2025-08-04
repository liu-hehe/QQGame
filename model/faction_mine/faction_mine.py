import model
from model.model_name import FactionMine


@model.RequestSend(cmd=FactionMine.cmd, op=FactionMine.op_reward)
def faction_mine():
    """矿洞/领取奖励"""
    return


@model.RequestSend(cmd=FactionMine.cmd, op=FactionMine.op_fight)
def faction_fight():
    """矿洞/挑战"""
    return


if __name__ == '__main__':
    faction_mine()
    for i in range(3):
        faction_fight()
