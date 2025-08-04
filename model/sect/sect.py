import model
from model.model_name import Sect


@model.RequestSend(cmd=Sect.cmd, op=Sect.op_training_with_npc)
def sect_training_with_npc():
    """门派/进入木桩训练免费挑战"""
    return


@model.RequestSend(cmd=Sect.cmd_shop, subtype=Sect.subtype, type=Sect.type_letter, times=Sect.times,
                   costtype=Sect.costtype)
def sect_exchange_letter():
    """门派/商店换战书"""
    return


@model.RequestSend(cmd=Sect.cmd, op=Sect.op_training_with_member)
def sect_training_with_member():
    """门派/进入同门切磋免费挑战"""
    return


@model.RequestSend(cmd=Sect.cmd, op=Sect.op_fumigate_free_incense)
def sect_fumigate_free_incense():
    """门派/普通香炉"""
    return


@model.RequestSend(cmd=Sect.cmd_shop, subtype=Sect.subtype, type=Sect.type, times=Sect.times, costtype=Sect.costtype)
def sect_exchange_incense():
    """门派/商店换香炉"""
    return


@model.RequestSend(cmd=Sect.cmd, op=Sect.op_fumigate_paid_incense)
def sect_fumigate_paid_incense():
    """门派/高香香炉"""
    return


@model.RequestSend(cmd=Sect.cmd_task)
def sect_fumigate_task_id():
    """门派/获取task_id"""
    return


@model.RequestSend(cmd=Sect.cmd, op=Sect.op_training_with_council)
def sect_fumigate_challenge_boss():
    """门派/挑战boss"""
    return


@model.RequestSend(cmd=Sect.cmd_task, subtype=Sect.subtype)
def sect_fumigate_task_complete():
    """门派/完成任务"""
    return

if __name__ == '__main__':

    sect_training_with_npc()  # 进入木桩训练免费挑战
    for i in range(3):
        response = sect_training_with_member()  # 进入同门切磋免费挑战
        if Sect.other_case in response.raw_rsp.text:
            sect_exchange_letter()
    sect_fumigate_free_incense()  # 普通香炉
    for i in range(2):
        response = sect_fumigate_paid_incense()  # 高香香炉
        if Sect.other_case_paid in response.raw_rsp.text:
            sect_exchange_incense()
    for i in range(1, 4):
        sect_fumigate_challenge_boss(rank=i, pos=i)  # 挑战三个boss

    response = sect_fumigate_task_id().raw_rsp.text  # 根据任务进入地方
    for k, v in Sect.action_list.items():
        if k in response:
            sect_fumigate_task_id(v)

    task_id = sect_fumigate_task_id(re_exp=Sect.complete_id)  # 查找已完成任务id
    if task_id:
        [sect_fumigate_task_complete(task_id=int(n)) for n in task_id]  # 完成任务
