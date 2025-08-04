import model
from model.model_name import Immortals


@model.RequestSend(cmd=Immortals.cmd, op=Immortals.op_get_reward, taskid=Immortals.task_id)
def immortals_get_reward():
    """仙武修真/领取80活跃度挑战次数"""
    return


@model.RequestSend(cmd=Immortals.cmd, re_exp=Immortals.re_exp)
def immortals_get_fight_times():
    """仙武修真/获取挑战次数"""
    return


@model.RequestSend(cmd=Immortals.cmd, op=Immortals.op_visit_immortals, mountainId=Immortals.mountainId)
def immortals_visit():
    """仙武修真/寻访"""
    return


@model.RequestSend(cmd=Immortals.cmd, op=Immortals.op_fight_immortals)
def immortals_fight():
    """仙武修真/挑战"""
    return


if __name__ == '__main__':
    immortals_get_reward()
    fight_times = immortals_get_fight_times()
    if fight_times and int(fight_times[0]) != 0:
        for i in range(int(fight_times[0])):
            immortals_visit()
            immortals_fight()
