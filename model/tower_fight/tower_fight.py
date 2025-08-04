import model
from model.model_name import TowerFight


@model.RequestSend(cmd=TowerFight.cmd, type=TowerFight.type_auto)
def tower_fight_auto():
    """斗神塔/自动挑战"""
    return


@model.RequestSend(cmd=TowerFight.cmd, type=TowerFight.type_finish, confirm=TowerFight.confirm)
def tower_fight_finish():
    """斗神塔/结束挑战"""
    return


if __name__ == '__main__':
    tower_fight_auto()
    tower_fight_finish()