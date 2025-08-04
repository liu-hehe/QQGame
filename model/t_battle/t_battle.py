import model
from model.model_name import TBattle


@model.RequestSend(cmd=TBattle.cmd, op=TBattle.op_draw_reward)
def t_battle_draw_reward():
    """问鼎天下/领取奖励"""
    return


@model.RequestSend(cmd=TBattle.cmd, op=TBattle.op_draw_release_reward)
def t_battle_op_draw_release_reward():
    """问鼎天下/资源奖励"""
    return


@model.RequestSend(cmd=TBattle.cmd, op=TBattle.op_show_region)
def t_battle_get_resource_id(**kwargs):
    """问鼎天下/获取资源id"""
    return


@model.RequestSend(re_exp=TBattle.re_exp_region, cmd=TBattle.cmd)
def t_battle_get_region_name():
    """问鼎天下/获取标记区域名字"""
    return


@model.RequestSend(cmd=TBattle.cmd, op=TBattle.op_occupy)
def t_battle_occupy_region(**kwargs):
    """问鼎天下/攻占资源"""
    return


if __name__ == '__main__':
    t_battle_draw_reward()  # 领取奖励
    t_battle_op_draw_release_reward()  # 资源奖励
    region_name = t_battle_get_region_name()  # 区域名字
    region_id_list = TBattle.region_id_list  # 区域id集合
    region_id = region_id_list.get(region_name[0]) if region_name else None  # 获取区域id
    re_exp_battle = fr'id=(\w+)&amp;region={region_id}">攻占'
    resource_id_list = t_battle_get_resource_id(re_exp=re_exp_battle, region=region_id)  # 获取资源id集合
    resource_id = resource_id_list[-1] if resource_id_list else None  # 获取资源id
    t_battle_occupy_region(id=resource_id, region=region_id)  # 攻占资源
