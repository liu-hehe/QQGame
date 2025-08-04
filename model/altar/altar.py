import model
from model.model_name import Altar


@model.RequestSend(cmd=Altar.cmd, op=Altar.op_draw_reward)
def altar_get_reward():
    """帮派祭坛/领取奖励"""
    return


@model.RequestSend(re_exp=Altar.turn_times, cmd=Altar.cmd, B_UID=Altar.B_UID)
def altar_get_times():
    """帮派祭坛/获取转动次数"""
    return


@model.RequestSend(re_exp=Altar.chose_fac_id, cmd=Altar.cmd, B_UID=Altar.B_UID)
def altar_chose_page():
    """帮派祭坛/转到选择帮派页面"""
    return


@model.RequestSend(cmd=Altar.cmd, op=Altar.op_spin_wheel)
def altar_turn():
    """帮派祭坛/转动轮盘"""
    return


@model.RequestSend(re_exp=Altar.chose_fac_id,cmd=Altar.cmd, op=Altar.op_spin_wheel)
def altar_turn_get_fac_id():
    """帮派祭坛/转到帮派页面获取帮派id"""
    return


@model.RequestSend(cmd=Altar.cmd, op=Altar.op_rob)
def altar_chose():
    """帮派祭坛/选择帮派挑战"""
    return


@model.RequestSend(cmd=Altar.cmd, op=Altar.op_steal)
def altar_chose_steal():
    """帮派祭坛/选择帮派偷取"""
    return


@model.RequestSend(cmd=Altar.cmd, op=Altar.op_do_steal)
def altar_chose_forward():
    """帮派祭坛/选择前进方向"""
    return


if __name__ == '__main__':
    altar_get_reward()  # 领取奖励
    turn_times = altar_get_times()  # 获取转动次数
    if not turn_times:
        fac_id_list = altar_turn(re_exp=Altar.chose_fac_id)  # 转到选择帮派页面
        altar_chose(id=int(fac_id_list[0]))  # 选择帮派挑战
        altar_chose_steal(id=int(fac_id_list[0]))  # 选择帮派偷取
        altar_chose_forward(id=int(fac_id_list[0]))  # 选择前进方向
    get_turn_times = altar_get_times()  # 获取转动次数
    turn_times = int(get_turn_times[0]) if get_turn_times else None
    print(turn_times)
    if turn_times:
        while turn_times > 0:
            turn_times -= 1  # 每次转动减1
            response = altar_turn()  # 转动轮盘
            if not response:
                continue
            if Altar.chose_fac in response.raw_rsp.text:  # 转到选择帮派页面
                fac_id_list = altar_turn(re_exp=Altar.chose_fac_id)
                altar_chose(id=int(fac_id_list[0]))  # 选择帮派挑战
                altar_chose_steal(id=int(fac_id_list[0]))  # 选择帮派偷取
                altar_chose_forward(id=int(fac_id_list[0]))  # 选择前进方向
            if Altar.change_times in response.raw_rsp.text:
                turn_times += 3  # 转动次数+3
            if Altar.change_times_one in response.raw_rsp.text:
                turn_times += 1  # 转动次数+1
