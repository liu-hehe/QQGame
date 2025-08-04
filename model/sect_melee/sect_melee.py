import model
from model.model_name import SectMelee


@model.RequestSend(cmd=SectMelee.cmd, op=SectMelee.op_draw_reward)
def sect_get_reward():
    """会武/领取奖励"""
    return


@model.RequestSend(re_exp=SectMelee.re_exp, cmd=SectMelee.cmd)
def sect_melee_id():
    """会武/获取场地id"""
    return


@model.RequestSend(cmd=SectMelee.cmd,op=SectMelee.op_show_scene)
def sect_melee_enter(**kwargs):
    """会武/进入场地"""
    return


@model.RequestSend(cmd=SectMelee.cmd,op=SectMelee.op_do_training)
def sect_melee_do_training():
    """会武/挑战"""
    return


@model.RequestSend(cmd=SectMelee.cmd,op=SectMelee.op_cheer, sect=SectMelee.sect)
def sect_melee_cheer():
    """会武/冠军助威"""
    return


if __name__ == '__main__':
    sect_get_reward()  # 领取奖励
    sect_melee_id = sect_melee_id()  # 获取场地id
    if sect_melee_id:
        for i in range(10):
            sect_melee_enter(scene=int(sect_melee_id[0]))  # 进入场地
            sect_melee_do_training()  # 挑战
    sect_melee_cheer()
