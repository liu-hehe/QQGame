import model
from model.model_name import Arena


@model.RequestSend(cmd=Arena.cmd, op=Arena.op_challenge)
def arena_challenge():
    """竞技场/免费挑战"""
    return


@model.RequestSend(cmd=Arena.cmd, op=Arena.op_draw_daily)
def arena_draw():
    """竞技场/领取奖励"""
    return


if __name__ == '__main__':
    for i in range(5):
        arena_challenge()
    arena_draw()