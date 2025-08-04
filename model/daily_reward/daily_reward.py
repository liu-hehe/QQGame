import model
from model.model_name import DailyReward


@model.RequestSend(cmd=DailyReward.cmd, op=DailyReward.op)
def daily_reward():
    """每日奖励/领取"""
    return


if __name__ == '__main__':
    for i in [DailyReward.key_login, DailyReward.key_meridian, DailyReward.key_daren, DailyReward.key_wu_zi_tian_shu]:
        daily_reward(key=i)