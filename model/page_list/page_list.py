import model
from model.model_name import Page


@model.RequestSend(cmd=Page.cmd)
def page_list():
    """主页活动列表"""
    return


@model.RequestSend()
def page_list_check():
    """主页活动/神魔转盘免费次数查询"""
    return


@model.RequestSend()
def page_list_check_machine():
    """主页活动/开心娃娃机免费次数查询"""
    return


@model.RequestSend()
def page_list_get_reward(**kwargs):
    """主页活动/领取奖励"""
    return


if __name__ == '__main__':
    response = page_list().raw_rsp.text
    for k, v in Page.page_dict.items():
        if k in response and k == Page.page_list[0]:  # 乐斗菜单
            [page_list_get_reward(gift=i) for i in range(1, 6)]
        elif k in response and k == Page.page_list[1]:  # 登录有礼
            [page_list_get_reward(v,gift_index=i) for i in range(6, -1, -1)]
        elif k in response and k == Page.page_list[2]:  # 神魔转盘
            if Page.check_str in page_list_check(v[1]):
                page_list_get_reward(v[0])
        elif k in response and k == Page.page_list[3]:  # 猜单双
            [page_list_get_reward(v) for i in range(6)]
        elif k in response and k == Page.page_list[4]:  # 开心娃娃机
            check_times = page_list_check_machine(v[1], re_exp=Page.check_times)
            if check_times and int(check_times[0]) == 1:
                page_list_get_reward(v[0])
        elif k in response and k not in Page.page_list:
            page_list_get_reward(v)
