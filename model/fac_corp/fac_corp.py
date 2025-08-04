import model
from model.model_name import FacCorp


@model.RequestSend(re_exp=FacCorp.re_exp, cmd=FacCorp.cmd, op=FacCorp.op_get_gift_id)
def fac_corp_gift_id_exp():
    """帮派商会/查询会过期奖励id"""
    return


@model.RequestSend(re_exp=FacCorp.re_not_exp, cmd=FacCorp.cmd, op=FacCorp.op_get_gift_id)
def fac_corp_gift_id_not_exp():
    """帮派商会/查询不会过期奖励id"""
    return


@model.RequestSend(cmd=FacCorp.cmd, op=FacCorp.op_get_gift)
def fac_corp_gift(**kwargs):
    """帮派商会/领取奖励"""
    return


if __name__ == '__main__':
    gift_id = fac_corp_gift_id_exp()  # 查询会过期奖励id
    if gift_id:
        [fac_corp_gift(gift_id=int(n), type=FacCorp.type_exp) for n in gift_id]
    gift_id = fac_corp_gift_id_not_exp()  # 查询不会过期奖励id
    print(gift_id)
    if gift_id:
        [fac_corp_gift(gift_id=int(n), type=FacCorp.type_not_exp) for n in gift_id]