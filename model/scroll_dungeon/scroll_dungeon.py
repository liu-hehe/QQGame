import model
from model.model_name import ScrollDungeon


@model.RequestSend(cmd=ScrollDungeon.cmd)
def scroll_dungeon_buff_chose(**kwargs):
    """画卷迷踪/buff选择"""
    return


@model.RequestSend(cmd=ScrollDungeon.cmd, op=ScrollDungeon.op_fight)
def scroll_dungeon_fight(**kwargs):
    """画卷迷踪/挑战"""
    return


if __name__ == '__main__':
    while True:
        gift_name = ScrollDungeon.gift_name
        for i in range(1, 7):
            scroll_dungeon_buff_chose(buff=i)
            response = scroll_dungeon_fight(re_exp=gift_name, buff=i)
            if gift_name not in response.raw_rsp.text:
                break
        response = scroll_dungeon_fight(re_exp=gift_name, buff=0)
        if gift_name not in response.raw_rsp.text:
            break
