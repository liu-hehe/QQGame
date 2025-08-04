import model
from model.model_name import Cargo


@model.RequestSend(cmd=Cargo.cmd, B_UID=Cargo.B_UID)
def cargo_get_info(**kwargs):
    """镖行天下/进入"""
    return


@model.RequestSend(cmd=Cargo.cmd, op=Cargo.op)
def cargo_get_reward_info(**kwargs):
    """镖行天下/获取奖励信息"""
    return

@model.RequestSend(re_exp=r'免费刷新次数：(\w+)<', cmd=Cargo.cmd, op=Cargo.op)
def cargo_get_refresh_reward_times(**kwargs):
    """镖行天下/获取刷新奖励次数"""
    return


@model.RequestSend(cmd=Cargo.cmd, op=Cargo.op_refresh)
def cargo_refresh_reward(**kwargs):
    """镖行天下/刷新奖励信息"""
    return


@model.RequestSend(cmd=Cargo.cmd, op=Cargo.op_transport)
def cargo_transport_reward(**kwargs):
    """镖行天下/启程护送"""
    return


@model.RequestSend(cmd=Cargo.cmd, op=Cargo.op_complete)
def cargo_transport_reward_complete(**kwargs):
    """镖行天下/护送完成"""
    return


@model.RequestSend(cmd=Cargo.cmd, op=Cargo.op_receive)
def cargo_transport_receive_reward(**kwargs):
    """镖行天下/领取奖励"""
    return


if __name__ == '__main__':
    #  获取之前的奖励
    cargo_get_info()
    cargo_transport_reward_complete()
    cargo_transport_receive_reward()
    # 开始护送新的奖励
    get_reward_info = cargo_get_reward_info()  # 获取奖励信息
    refresh_reward_times = cargo_get_refresh_reward_times()  # 获取刷新奖励次数
    if refresh_reward_times:
        for i in range(int(refresh_reward_times[0])):
            if Cargo.reward in get_reward_info:  # 刷到最好的奖励
                cargo_transport_reward()  # 启程护送
                break
            else:
                cargo_refresh_reward()  # 刷新奖励
        cargo_transport_reward()  # 启程护送
