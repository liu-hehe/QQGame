import model
from model.model_name import WlMeeting


@model.RequestSend(cmd=WlMeeting.cmd, ifFirstSign=WlMeeting.ifFirstSign, B_UID=WlMeeting.B_UID)
def wl_meeting():
    """武林大会/报名"""
    return


if __name__ == '__main__':
    wl_meeting()