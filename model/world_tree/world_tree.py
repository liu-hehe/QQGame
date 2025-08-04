import model
from model.model_name import WorldTree


@model.RequestSend(cmd=WorldTree.cmd, B_UID=WorldTree.B_UID)
def world_tree_into():
    """世界树/进入"""
    return


@model.RequestSend(cmd=WorldTree.cmd, op=WorldTree.op_tree)
def world_tree_enter():
    """世界树/进入奇树灵鉴"""
    return


@model.RequestSend(cmd=WorldTree.cmd, op=WorldTree.op_tree, type=WorldTree.type)
def world_tree_fu_bao():
    """世界树/奇树灵鉴/进入福宝"""
    return


@model.RequestSend(cmd=WorldTree.cmd, op=WorldTree.op_auto_get, id=WorldTree.id)
def world_tree_auto_get():
    """世界树/奇树灵鉴/福宝/一键领取经验"""
    return


@model.RequestSend(re_exp=WorldTree.re_exp, cmd=WorldTree.cmd, op=WorldTree.op_weapon_id)
def get_weapon_id_back():
    """免费温养获取weapon_id"""
    return


@model.RequestSend(cmd=WorldTree.cmd, op=WorldTree.op_do_strengh, times=WorldTree.time)
def world_tree_do_strengh(**kwargs):
    """世界树/奇树灵鉴/福宝/源宝树/免费温养一次"""
    return


if __name__ == '__main__':
    world_tree_into()
    world_tree_enter()
    world_tree_fu_bao()
    world_tree_auto_get()
    world_tree_do_strengh(weapon_id=int(get_weapon_id_back()[0]))