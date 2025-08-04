import model
import re
from model.model_name import SpaceRelic


@model.RequestSend(cmd=SpaceRelic.cmd_space_relic, op=SpaceRelic.op_relic_index)
def space_relic_enter():
    """时空遗迹/进入遗迹征伐"""
    return


@model.RequestSend(cmd=SpaceRelic.cmd_space_relic, op=SpaceRelic.op_monster)
def space_relic_enter_challenge():
    """时空遗迹/遗迹征伐/进入异兽洞窟"""
    return


@model.RequestSend(cmd=SpaceRelic.cmd_space_relic, op=SpaceRelic.op_monster_fight)
def space_relic_challenge(**kwargs):
    """时空遗迹/遗迹征伐/异兽洞窟/挑战"""
    return


@model.RequestSend(cmd=SpaceRelic.cmd_space_relic, op=SpaceRelic.op_boss_fight)
def space_relic_show_union(**kwargs):
    """时空遗迹/遗迹征伐/联合征伐/挑战"""
    return


@model.RequestSend(cmd=SpaceRelic.cmd_space_relic, op=SpaceRelic.op_task, type=SpaceRelic.type_week)
def space_relic_week_task(**kwargs):
    """时空遗迹/悬赏任务/每周任务/领取"""
    return


@model.RequestSend(cmd=SpaceRelic.cmd_space_relic, op=SpaceRelic.op_task, type=SpaceRelic.type_season)
def space_relic_season_task():
    """时空遗迹/悬赏任务/赛季任务/领取"""
    return


if __name__ == '__main__':
    space_relic_enter()
    space_relic_enter_challenge()
    for i in range(1, 6):
        space_relic_challenge(id=i)
    space_relic_show_union()
    [space_relic_week_task(id=i) for i in range(1, 4)]
    [space_relic_season_task(id=i) for i in range(4, 9)]
