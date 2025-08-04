import model
from model.model_name import FactionArmy


@model.RequestSend(cmd=FactionArmy.cmd, op=FactionArmy.op_get_point_award)
def faction_army_point_award(**kwargs):
    """帮派远征军/领取奖励"""
    return


@model.RequestSend(cmd=FactionArmy.cmd, op=FactionArmy.op_getIslandAward)
def faction_army_island_award(**kwargs):
    """帮派远征军/领取宝箱"""
    return


if __name__ == '__main__':
    for i in range(FactionArmy.point_id):
        faction_army_point_award(point_id=i)
    for n in range(FactionArmy.island_id):
        faction_army_island_award(island_id=n)