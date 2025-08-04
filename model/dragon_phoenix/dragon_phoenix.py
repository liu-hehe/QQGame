from public_common.request import HTTPRequester
import model
from model.model_name import DragonPhoenix


@model.RequestSend(cmd=DragonPhoenix.cmd, op=DragonPhoenix.op_gift)
def dragon_phoenix_gift():
    """龙凰论武每日领奖"""
    return


@model.RequestSend(cmd=DragonPhoenix.cmd, op=DragonPhoenix.op_rank_reward)
def dragon_phoenix_rank_reward():
    """龙凰论武赛季领奖"""
    return


def dragon_phoenix_challenge():
    # 龙凰论武剩余挑战次数
    url = model.url
    params = {'zapp_uin': '', 'sid': '', 'channel': 0, 'g_ut': 1, 'cmd': 'dragonphoenix', 'op': 'lunwu'}
    response = HTTPRequester().send('get', url=url, params=params)
    return response


if __name__ == '__main__':
    print(dragon_phoenix_gift())
