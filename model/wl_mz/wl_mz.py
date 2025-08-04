import model
from model.model_name import WlMz


@model.RequestSend(cmd=WlMz.cmd, op=WlMz.op_view_index)
def wl_mz_view_get_id():
    """武林盟主/获取奖励id"""
    return


@model.RequestSend(cmd=WlMz.cmd, op=WlMz.op_view_index)
def wl_mz_view():
    """武林盟主/查看是否报名时间"""
    return


@model.RequestSend(cmd=WlMz.cmd, op=WlMz.op_signup, ground_id=WlMz.ground_id)
def wl_mz_sigh_up():
    """武林盟主/报名"""
    return


@model.RequestSend(cmd=WlMz.cmd, op=WlMz.op_get_award, section_id=WlMz.section_id)
def wl_mz_get_award():
    """武林盟主/获取奖励"""
    return


@model.RequestSend(cmd=WlMz.cmd, op=WlMz.op_view_guess)
def wl_mz_guess():
    """武林盟主/前往竞猜"""
    return


@model.RequestSend(cmd=WlMz.cmd, op=WlMz.op_guess_up)
def wl_mz_guess_up(**kwargs):
    """武林盟主/前往竞猜/选择玩家"""
    return


@model.RequestSend(cmd=WlMz.cmd, op=WlMz.op_confirm)
def wl_mz_confirm():
    """武林盟主/前往竞猜/确认"""
    return


if __name__ == '__main__':

    response = wl_mz_view()
    if WlMz.check_str in response.raw_rsp.text:  # 武林盟主/报名
        wl_mz_sigh_up()
    else:
        get_id = wl_mz_view(re_exp=WlMz.get_id)
        wl_mz_get_award(section_id=int(get_id[0][0]), round_id=int(get_id[0][1])) if get_id else None  # 获取奖励
        wl_mz_guess()  # 前往竞猜
        for i in range(WlMz.index):
            wl_mz_guess_up(index=i)
        wl_mz_confirm()  # 前往竞猜/确认
