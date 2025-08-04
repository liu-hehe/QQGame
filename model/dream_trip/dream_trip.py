import model
from model.model_name import DreamTrip


@model.RequestSend(cmd=DreamTrip.cmd, sub=DreamTrip.sub)
def dream_trip():
    """梦想之旅/普通机票"""
    return


if __name__ == '__main__':
    dream_trip()