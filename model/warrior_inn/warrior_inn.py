import model
from model.model_name import WarriorInn


@model.RequestSend(re_exp=WarriorInn.re_exp, cmd=WarriorInn.cmd, B_UID=WarriorInn.B_UID)
def warrior_inn_enter_get_type(**kwargs):
    """侠士客栈/进入获取房间类型"""
    return


@model.RequestSend(cmd=WarriorInn.cmd, op=WarriorInn.op_get_lobby_reward)
def warrior_inn_get_reward(**kwargs):
    """侠士客栈/领取奖励"""
    return


if __name__ == '__main__':
    room_type = warrior_inn_enter_get_type()
    if room_type:
        get_reward_times = WarriorInn.num
        for i in range(get_reward_times):
            warrior_inn_get_reward(type=int(room_type[0]), num=i+1)