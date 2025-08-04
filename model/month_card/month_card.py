import model
from model.model_name import MonthCard


@model.RequestSend(cmd=MonthCard.cmd, sub=MonthCard.sub)
def month_card():
    """斗豆月卡/领取奖励"""
    return


if __name__ == '__main__':
    month_card()