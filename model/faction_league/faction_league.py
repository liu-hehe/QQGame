import model
from model.model_name import FactionLeague


@model.RequestSend(re_exp=FactionLeague.re_exp, cmd=FactionLeague.cmd, op=FactionLeague.op)
def faction_league_get_id():
    """帮派黄金联赛/领取奖励"""
    return


@model.RequestSend(cmd=FactionLeague.cmd)
def faction_league():
    """帮派黄金联赛/领取奖励"""
    return


if __name__ == '__main__':
    get_id = faction_league_get_id()
    faction_league(op=int(get_id[0])) if get_id else None
