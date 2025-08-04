import model
from model.model_name import FacChallenge


@model.RequestSend(cmd=FacChallenge.cmd, subtype=FacChallenge.subtype)
def fac_practice():
    """踢馆/试练"""
    return


@model.RequestSend(cmd=FacChallenge.cmd, B_UID=FacChallenge.B_UID, subtype=FacChallenge.subtype_table)
def fac_table():
    """踢馆/转盘"""
    return


@model.RequestSend(cmd=FacChallenge.cmd, B_UID=FacChallenge.B_UID, subtype=FacChallenge.subtype_challenge)
def fac_challenge():
    """踢馆/挑战"""
    return


@model.RequestSend(cmd=FacChallenge.cmd, B_UID=FacChallenge.B_UID, subtype_table=FacChallenge.subtype_reward)
def fac_reward():
    """踢馆/领奖"""
    return


@model.RequestSend(re_exp=FacChallenge.re_exp, cmd=FacChallenge.cmd, B_UID=FacChallenge.B_UID,
                   subtype=FacChallenge.subtype_rank_id)
def fac_rank_reward_id():
    """踢馆/排行奖励id查询"""
    return


@model.RequestSend(cmd=FacChallenge.cmd, B_UID=FacChallenge.B_UID)
def fac_rank_reward():
    """踢馆/排行奖励"""
    return


if __name__ == '__main__':
    import datetime
    reward_id = fac_rank_reward_id()  # 排行奖励id查询
    fac_rank_reward(subtype=int(reward_id[0])) if reward_id else None  # 排行奖励
    response = fac_reward()  # 领奖
    time = f'{datetime.datetime.now().month}月{datetime.datetime.now().day}日'
    if time in response.raw_rsp.text:
        for i in range(5):
            fac_practice()  # 试练
        fac_table()  # 转盘
        for i in range(3):
            fac_challenge()  # 挑战
