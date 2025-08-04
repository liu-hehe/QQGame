import model
from model.model_name import SectTournament


@model.RequestSend(cmd=SectTournament.cmd, op=SectTournament.op_signup)
def sect_tournament_signup():
    """门派邀请赛/组队报名"""
    return


@model.RequestSend(cmd=SectTournament.cmd, op=SectTournament.op_fight)
def sect_tournament():
    """门派邀请赛/开始挑战"""
    return


if __name__ == '__main__':
    sect_tournament_signup()
    for i in range(5):
        sect_tournament()