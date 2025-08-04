import model
from model.model_name import FacTask


@model.RequestSend(re_exp=r'id=(\w+)">', cmd=FacTask.cmd, sub=FacTask.sub)
def fac_task_id():
    """帮派任务id"""
    return


@model.RequestSend()
def fac_perform_task(*args):
    """执行帮派任务"""
    return


@model.RequestSend(cmd=FacTask.cmd, sub=FacTask.sub_reward)
def fac_reward():
    """领取帮派任务奖励"""
    return


if __name__ == '__main__':
    task_id_list = fac_task_id()
    if task_id_list:
        task_id = list(dict.fromkeys(task_id_list))  # 去重
        for i in task_id:
            if int(i) in FacTask.id.keys():
                param = FacTask.id.get(int(i))
                fac_perform_task(param)  # 执行帮派任务
                fac_reward(id=int(i))  # 领取帮派任务奖励
