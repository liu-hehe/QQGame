class DragonPhoenix:
    dragon_phoenix = '龙凰之境'
    cmd = 'dragonphoenix'
    op_gift = 'gift'  # 每日领奖
    op_rank_reward = 'rankreward'  # 赛季领奖


class WorldTree:
    world_tree = '世界树'
    type = 3
    B_UID = 0
    op_tree = 'tree'
    cmd = 'worldtree'
    op_auto_get = 'autoget'
    op_weapon_id = 'viewexpandindex'
    op_do_strengh = 'dostrengh'
    id = 1
    time = 1
    re_exp = r'weapon_id=(\w+)'


class SpaceRelic:
    space_relic = '时空遗迹'
    cmd_space_relic = 'spacerelic'
    op_monster = 'monster'
    op_relic_index = 'relicindex'
    op_monster_detail = 'monsterdetail'  # 获取挑战次数
    op_monster_fight = 'monsterfight'  # 挑战
    op_show_union = 'showunion'  # 每周任务奖励领取
    op_boss_fight = 'bossfight'  # 每赛季任务奖励领取
    challenge_num = r'剩余挑战次数：(\w)<br'
    op_task = 'task'
    type_week = 1
    type_season = 2

    knight_island = '侠客岛'

    enchant = '器魂附魔'


class AbyssTide:
    abyss_tide = '深渊之潮'
    cmd = 'abysstide'
    op_view_faction_gift = 'viewfactiongift'  # 进入帮派巡礼
    op_get_faction_gift = 'getfactiongift'  # 领取帮派巡礼
    op_view_all_abyss = 'viewallabyss'  # 进入深渊秘境，获取挑战次数
    op_enter_abyss = 'enterabyss'  # 已进入深渊秘境
    op_begin_fight = 'beginfight'  # 开始战斗
    op_confirm = 'confirm'  # 进入副本保存/通关后保存
    type_enter = 'enter'  # 是否进入副本
    type_settle = 'settle'  # 是否结算副本
    op_end_abyss = 'endabyss'  # 结算


class AscendHeaven:
    ascend_heaven = '飞升大作战'
    cmd = 'ascendheaven'
    op_view_sign_up = 'viewsignup'  # 是否报名
    type_rank = 1  # 排位
    op_sign_up = 'signup'  # 确认报名
    type_match = 2  # 匹配

    calender = '乐斗黄历'


class Immortals:
    immortals = '仙武修真'
    cmd = 'immortals'
    op_get_reward = 'getreward'  # 领取80活跃度挑战次数
    task_id = 1  # 领取80活跃度挑战次数
    op_visit_immortals = 'visitimmortals'  # 寻访
    mountainId = 2  # 访问的山名
    refresh_immortals = 'refreshimmortals'  # 刷新寻访
    op_fight_immortals = 'fightimmortals'  # 挑战
    re_exp = r'剩余挑战次数：(\w+)<br'

    new_Act = '神将月卡'

    jiang_hu_dream = '江湖长梦'


class WarriorInn:
    warrior_inn = '侠士客栈'
    cmd = 'warriorinn'
    re_exp = 'type=(\w+)'
    B_UID = 0
    op_get_lobby_reward = 'getlobbyreward'
    type = 1
    num = 3


class LuanDou:
    luan_dou = '全民乱斗'
    cmd = 'luandou'
    op = 8


class WlMz:
    wl_mz = '武林盟主'
    cmd = 'wlmz'
    op_view_index = 'view_index'  # 查看是否报名时间
    op_get_award = 'get_award'  # 获取奖励
    section_id = 4  # 获取奖励
    round_id = 1  # 获取奖励
    get_id = r'section_id=(\w+)&amp;round_id=(\w+)">领取奖励'  # 获取奖励id
    op_view_guess = 'view_guess'  # 前往竞猜
    op_guess_up = 'guess_up'  # 选择玩家
    op_confirm = 'comfirm'  # 确认玩家
    index = 8  # 八名玩家
    op_signup = 'signup'  # 报名
    ground_id = 1  # 报名
    check_str = '距离报名结束'

    mission_assign = '任务派遣中心'


class FactionLeague:
    faction_league = '帮派黄金联赛'
    cmd = 'factionleague'
    re_exp = r'op=(\w+)">'
    B_UID = 0
    op = 0


class FactionArmy:
    faction_army = '帮派远征军'
    cmd = 'factionarmy'
    op_view_index = 'viewIndex'
    op_get_point_award = 'getPointAward'  # 领取奖励
    point_id = 15  # 领取奖励
    op_getIslandAward = 'getIslandAward'  # 领取宝箱
    island_id = 5  # 领取宝箱


class FacCorp:
    fac_corp = '帮派商会'
    cmd = 'fac_corp'
    op_get_gift_id = 0
    op_get_gift = 3
    type_exp = 0  # 会过期奖励
    type_not_exp = 1  # 不会过期奖励
    re_exp = fr'gift_id=(\w+)&amp;type={type_exp}'
    re_not_exp = fr'gift_id=(\w+)&amp;type={type_not_exp}'


class TBattle:
    t_battle = '问鼎天下'
    cmd = 'tbattle'
    op_draw_reward = 'drawreward'  # 领取奖励
    op_draw_release_reward = 'drawreleasereward'  # 资源领取
    op_show_region = 'showregion'  # 查看区域资源
    region_id_list = {'东海': 1, '南荒': 2, '西泽': 3, '北寒': 4}  # 标记区域id集合
    re_exp_battle = r'id=(\w+)&amp;region=1">攻占'  # 获取资源id集合
    re_exp_region = r'>([\u4e00-\u9fa5]+)</a>\s*-已标记'  # 获取标记区域名字
    op_occupy = 'occupy'  # 攻占资源''


class DreamTrip:
    dream_trip = '梦想之旅'
    cmd = 'dreamtrip'
    sub = 2


class SectMelee:
    sect_melee = '会武'
    cmd = 'sectmelee'
    op_draw_reward = 'drawreward'  # 获取奖励
    re_exp = r'op=showscene&amp;scene=(\w+)">'
    op_show_scene = 'showscene'  # 进入场地
    scene = 'scene'  # 场地id
    op_do_training = 'dotraining'  # 挑战
    op_cheer = 'cheer'
    sect = 1003


class Altar:
    altar = '帮派祭坛'
    cmd = 'altar'
    B_UID = 0
    op_draw_reward = 'drawreward'  # 领取奖励
    turn_times = r'剩余次数：(\w+)<br'  # 获取转动轮盘次数
    op_spin_wheel = 'spinwheel'  # 转动轮盘
    change_times = '获得转盘次数*3'
    change_times_one = '返还你一次轮盘次数'
    chose_fac = '随机分配'  # 随机选择帮派
    chose_fac_id = r'id=(\w+)">选择'  # 获取帮派id
    op_steal = 'steal'  # 选择帮派偷取
    op_do_steal = 'dosteal'  # 选择前进方向
    op_rob = 'rob'  # 选择帮派偷取，不需要选前进方向


class SectTournament:
    sect_tournament = '门派邀请赛'
    cmd = 'secttournament'
    op_fight = 'fight'
    op_signup = 'signup'  # 组队报名


class Sect:
    sect = '门派'
    cmd = 'sect'
    task_dict = {118: {'showcouncil': {'rank': 3, 'pos': 1}}, 120: 'showfumigate',
                 106: {'showcouncil': {'rank': 3, 'pos': 1}}}
    op_training_with_npc = 'trainingwithnpc'  # 进入木桩训练免费挑战
    op_training_with_member = 'trainingwithmember'  # 进入同门切磋免费挑战
    type_letter = 1249  # 门派战书
    op_fumigate_free_incense = 'fumigatefreeincense'  # 普通香炉
    op_fumigate_paid_incense = 'fumigatepaidincense'  # 高香香炉
    cmd_shop = 'exchange'  # 商店换门派高香
    other_case = '门派战书数量不足'
    other_case_paid = '门派高香数量不足'
    op_training_with_council = 'trainingwithcouncil'  # 挑战boss
    complete_id = r'task_id=(\w+)">完成'  # 查找已完成任务id
    cmd_task = 'sect_task'  # 完成任务
    action_list = {'华藏寺': {'cmd': 'sect_art'}, '伏虎寺': {'cmd': 'sect_trump'},
                   '金顶': {'cmd': 'sect', 'op': 'showcouncil'}, '五花堂': {'cmd': 'sect_task'},
                   '八叶堂': {'cmd': 'sect', 'op': 'showtraining'}, '万年寺': {'cmd': 'sect', 'op': 'showfumigate'}}
    rank = 1
    subtype = 2
    type = 1248
    times = 1
    costtype = 11


class ScrollDungeon:
    scroll_dungeon = '画卷迷踪'
    cmd = 'scroll_dungeon'
    op_fight = 'fight'
    buff = 0
    fame_hall = '名人堂'
    gift_name = '百炼钢'


class ThronesBattle:
    thrones_battle = '群雄逐鹿'
    cmd = 'thronesbattle'  # 报名
    op_signup = 'signup'  # 报名
    op_draw_reward = 'drawreward'  # 领奖
    op_draw_rank_reward = 'drawrankreward'  # 排行榜领奖


class Misty:
    misty = '幻境'
    cmd = 'misty'
    B_UID = 0
    op_start = 'start'
    op_fight = 'fight'
    op_return = 'return'

    achievement = '徽章馆'


class Cargo:
    cargo = '镖行天下'
    cmd = 'cargo'
    B_UID = 0
    op = 7  # 获取奖励信息
    reward = '经验*1425,孙子兵法*15,武穆遗书*15,威望*561'
    op_refresh = 8  # 刷新奖励信息
    op_transport = 6  # 启程护送
    op_complete = 15  # 护送完成
    op_receive = 16  # 领取奖励

    tuan_gou = '团购'

    task = '任务'


class MapPush:
    map_push = '任务'
    cmd = 'mappush'
    B_UID = 0
    subtype = 1
    area_subtype = 2
    challenge_subtype = 3
    mapid = 20
    pageid = 2
    npcid_next = 6393
    npcid = 6394

    month_first_pay = '月首兑'


class TowerFight:
    tower_fight = '斗神塔'
    cmd = 'towerfight'
    type_auto = 11  # 自动挑战
    type_finish = 7  # 结束挑战
    confirm = 1  # 结束挑战


class RecommendManor:
    recommend_manor = '抢地盘'
    cmd = 'manorget'
    type = 1

    wish = '许愿'

    callback = '重出江湖'


class ZodiacDungeon:
    zodiac_dungeon = '十二宫'
    cmd = 'zodiacdungeon'
    op_show_fight_page = 'showfightpage'
    scene_id = 1011
    op_auto_fight = 'autofight'
    pay_recover_times = 0  # 普通扫荡


class Arena:
    arena = '竞技场'
    cmd = 'arena'
    op_challenge = 'challenge'
    op_draw_daily = 'drawdaily'


class FacChallenge:
    fac_challenge = '踢馆'
    cmd = 'facchallenge'  # 试练
    subtype = 2  # 试练
    B_UID = 0
    subtype_table = 4  # 转盘
    subtype_challenge = 3  # 挑战
    subtype_reward = 7  # 领奖
    subtype_rank_id = 10  # 排行奖励id
    re_exp = r'subtype=(\w+)">领取奖励'


class ForageWar:
    forage_war = '掠夺'
    cmd = 'forage_war'
    subtype = 6


class FactionMine:
    faction_mine = '矿洞'
    cmd = 'factionmine'
    op_reward = 'reward'
    op_fight = 'fight'

    view_shop = '商店'


class MonthCard:
    month_card = '斗豆月卡'
    cmd = 'monthcard'
    sub = 1


class DailyChest:
    daily_chest = '每日宝箱'
    cmd = 'dailychest'
    op = 'open'
    type_copper = 0
    type_silver = 1
    type_gold = 2

    birthday = '生日'


class TenLottery:
    ten_lottery = '邪神秘宝'
    cmd = 'tenlottery'
    op = 2
    type_high = 0
    type_best = 1


class KnightArena:
    knight_arena = '华山论剑'
    cmd = 'knightarena'
    op = 'challenge'


class WlMeeting:
    fast_sign_wu_lin = '武林大会'
    B_UID = 0
    cmd = 'fastSignWulin'
    ifFirstSign = 1


class FacTask:
    cmd = 'factiontask'
    sub = 1  # 帮派任务id
    sub_reward = 3  # 领取奖励
    id = {1: {'cmd': 'oblation', 'id': 3016, 'page': 2},  # 供奉
          10: {'cmd': 'factionmine'},  # 矿洞
          11: {'cmd': 'factionhr', 'subtype': 14},  # 帮贡
          12: {'cmd': 'facwar', 'sub': 0, 'id': 1},  # 帮战
          13: {'cmd': 'forage_war'},  # 掠夺
          14: {'cmd': 'facwar', 'sub': 2, 'id': 1},  # 帮战冠军
          15: {'cmd': 'use', 'id': 3038, 'store_type': 0, 'page': 1},  # 使用贡献药水
          16: {'cmd': 'factionop', 'subtype': 8, 'pageno': 1, 'type': 2},  # 要闻
          }


class DailyReward:
    cmd = 'dailygift'  # 领取每日奖励
    op = 'draw'
    key_login = 'login'
    key_meridian = 'meridian'
    key_daren = 'daren'
    key_wu_zi_tian_shu = 'wuzitianshu'


class Page:
    cmd = 'index'  # 主页活动
    page_dict = {'乐斗菜单': {'cmd': 'menuact', 'sub': 1}, '幸运转盘': {'cmd': 'newAct', 'subtype': 57, 'op': 'roll'},
                 '登录有礼': {'cmd': 'newAct', 'subtype': 56, 'op': 'draw', 'gift_type': 1},
                 '神魔转盘': [{'cmd': 'newAct', 'subtype': 88, 'op': 1},
                          {'B_UID': 0, 'cmd': 'newAct', 'subtype': 88, 'op': 0}],
                 '开心娃娃机': [{'cmd': 'newAct', 'subtype': 124, 'op': 1},{'cmd': 'newAct', 'subtype': 124, 'op': 0}],
                 '浩劫宝箱': {'B_UID': 0, 'cmd': 'newAct', 'subtype': 152},
                 '猜单双': {'cmd': 'oddeven','value': 1}}

    page_list = ['乐斗菜单', '登录有礼', '神魔转盘', '猜单双', '开心娃娃机']

    check_str = '免费抽奖一次'  # 神魔转盘
    check_times = r'免费次数：(\w+)/1<br'  # 开心娃娃机


class MenuAct:
    menu_act = '乐斗菜单'
    cmd = 'menuact'  # 乐斗菜单
    sub = 1


class LuckyTurn:
    lucky_turn = '幸运转盘'
    cmd = 'newAct'
    subtype = 57
    op = 'roll'


class ChallengeBoss:
    cmd = 'fight'  # 乐斗帮派boss和乐斗boss
    B_UID_WITHOUT_EXP = [10, 2, 3, 4, 5, 6, 14, 19, 155, 156, 152, 15, 13]
    B_UID_EXP = [161, 33, 16, 12, 11, 9, 7, 151]
    type = 2
    page = 1
