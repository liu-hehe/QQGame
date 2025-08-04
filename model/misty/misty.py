import model
from model.model_name import Misty


@model.RequestSend(cmd=Misty.cmd, B_UID=Misty.B_UID, op=Misty.op_return)
def misty_return():
    """幻境/返回幻境"""
    return


@model.RequestSend(re_exp=r'stage_id=(\w+)">', cmd=Misty.cmd)
def misty_get_id():
    """幻境/获取id"""
    return


@model.RequestSend(cmd=Misty.cmd, B_UID= Misty.B_UID, op=Misty.op_start)
def misty_entry():
    """幻境/进入"""
    return


@model.RequestSend(cmd=Misty.cmd, op=Misty.op_fight)
def misty_fight():
    """幻境/挑战"""
    return


if __name__ == '__main__':
    misty_id = misty_get_id()
    if misty_id:
        misty_entry(stage_id=int(misty_id[-1]))
        [misty_fight() for i in range(5)]