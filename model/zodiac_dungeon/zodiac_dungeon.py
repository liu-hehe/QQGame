import model
from model.model_name import ZodiacDungeon


@model.RequestSend(cmd=ZodiacDungeon.cmd, op=ZodiacDungeon.op_show_fight_page, scene_id=ZodiacDungeon.scene_id)
def zodiac_dungeon():
    """十二宫/双鱼宫扫荡"""
    return


@model.RequestSend(cmd=ZodiacDungeon.cmd, op=ZodiacDungeon.op_auto_fight, scene_id=ZodiacDungeon.scene_id,
                   pay_recover_times=ZodiacDungeon.pay_recover_times)
def zodiac_dungeon_normal():
    """十二宫/双鱼宫普通扫荡"""
    return


if __name__ == '__main__':
    zodiac_dungeon_normal()