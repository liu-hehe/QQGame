import model
from model.model_name import ChallengeBoss


@model.RequestSend(cmd=ChallengeBoss.cmd, type=ChallengeBoss.type)
def challenge_boss():
    """帮派/好友/boss乐斗"""
    return


if __name__ == '__main__':
    for i in ChallengeBoss.B_UID_WITHOUT_EXP:
        challenge_boss(B_UID=i)
    for i in ChallengeBoss.B_UID_EXP:
        challenge_boss(B_UID=i)