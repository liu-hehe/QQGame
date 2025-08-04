import model
from model.model_name import MenuAct
from model.model_name import Page


@model.RequestSend(cmd=Page.cmd)
def page_list():
    """主页活动列表"""
    return


@model.RequestSend(cmd=MenuAct.cmd, sub=MenuAct.sub)
def menu_act(**kwargs):
    """乐斗菜单/领取奖励"""
    return


if __name__ == '__main__':
    response = page_list().raw_rsp.text
    if MenuAct.menu_act in response:
        [menu_act(gift=i) for i in range(1, 6)]
