import model
from model.model_name import ThronesBattle


@model.RequestSend(cmd=ThronesBattle.cmd)
def thrones_battle_enter():
    """群雄逐鹿/进入"""
    return

@model.RequestSend(cmd=ThronesBattle.cmd, op=ThronesBattle.op_signup)
def thrones_battle_signup():
    """群雄逐鹿/报名"""
    return


@model.RequestSend(cmd=ThronesBattle.cmd, op=ThronesBattle.op_draw_reward)
def thrones_battle_draw_reward():
    """群雄逐鹿/领奖"""
    return


@model.RequestSend(cmd=ThronesBattle.cmd, op=ThronesBattle.op_draw_rank_reward)
def thrones_battle_rank_draw_reward():
    """群雄逐鹿/排行榜领奖"""
    return


if __name__ == '__main__':
    thrones_battle_signup()
    thrones_battle_enter()
    thrones_battle_draw_reward()
    thrones_battle_rank_draw_reward()