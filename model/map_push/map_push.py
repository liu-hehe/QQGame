import model
from model.model_name import MapPush


@model.RequestSend(cmd=MapPush.cmd, B_UID=MapPush.B_UID, subtype=MapPush.subtype)
def map_push_enter(**kwargs):
    """历练/进入"""
    return


@model.RequestSend(cmd=MapPush.cmd, subtype=MapPush.area_subtype, mapid=MapPush.mapid, pageid=MapPush.pageid)
def map_push_enter_area(**kwargs):
    """历练/进入场地"""
    return


@model.RequestSend(cmd=MapPush.cmd, subtype=MapPush.challenge_subtype, mapid=MapPush.mapid, pageid=MapPush.pageid)
def map_push_challenge(**kwargs):
    """历练/挑战"""
    return


if __name__ == '__main__':
    for i in range(5):
        if i == 3 or i == 4:
            map_push_challenge(npcid=MapPush.npcid_next)
        else:
            map_push_challenge(npcid=MapPush.npcid)