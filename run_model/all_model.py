import run_model


def func_pass(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception:
            pass
    return wrapper


class RunModel:
    def __init__(self):
        self.run_way = run_model

    def run_abyss_tide(self):
        # 深渊之潮/帮派巡礼领取-深渊秘境进入挑战-结算副本
        self.run_way.abyss_tide.abyss_tide_gift()
        times = self.run_way.abyss_tide.abyss_tide_times()
        if times:
            for i in range(int(times[0])):
                self.run_way.abyss_tide.abyss_tide_enter()
                self.run_way.abyss_tide.abyss_tide_enable()
                for i in range(5):
                    self.run_way.abyss_tide.abyss_tide_fight()
                self.run_way.abyss_tide.abyss_tide_settle()
                self.run_way.abyss_tide.abyss_tide_end_abyss()
        else:
            pass

    def run_altar(self):
        # 帮派祭坛/领取奖励-转动轮盘
        self.run_way.altar.altar_get_reward()  # 领取奖励
        turn_times = self.run_way.altar.altar_get_times()  # 获取转动次数
        if not turn_times:
            fac_id_list = self.run_way.altar.altar_chose_page()  # 转到选择帮派页面
            self.run_way.altar.altar_chose(id=int(fac_id_list[0]))  # 选择帮派挑战
            self.run_way.altar.altar_chose_steal(id=int(fac_id_list[0]))  # 选择帮派偷取
            self.run_way.altar.altar_chose_forward(id=int(fac_id_list[0]))  # 选择前进方向
        get_turn_times = self.run_way.altar.altar_get_times()  # 获取转动次数
        turn_times = int(get_turn_times[0]) if get_turn_times else None
        if turn_times:
            while turn_times > 0:
                turn_times -= 1  # 每次转动减1
                response = self.run_way.altar.altar_turn()  # 转动轮盘
                if self.run_way.altar.Altar.chose_fac in response.raw_rsp.text:  # 转到选择帮派页面
                    fac_id_list = self.run_way.altar.altar_turn_get_fac_id()  # 转到帮派页面获取帮派id
                    self.run_way.altar.altar_chose(id=int(fac_id_list[0]))  # 选择帮派挑战
                    self.run_way.altar.altar_chose_steal(id=int(fac_id_list[0]))  # 选择帮派偷取
                    self.run_way.altar.altar_chose_forward(id=int(fac_id_list[0]))  # 选择前进方向
                if self.run_way.altar.Altar.change_times in response.raw_rsp.text:
                    turn_times += 3  # 转动次数+3
                if self.run_way.altar.Altar.change_times_one in response.raw_rsp.text:
                    turn_times += 1  # 转动次数+1

    def run_arena(self):
        # 竞技场/免费挑战-领取奖励
        for i in range(5):
            self.run_way.arena.arena_challenge()
        self.run_way.arena.arena_draw()

    def run_ascend_heaven(self):
        # 飞升大作战/报名
        self.run_way.ascend_heaven.ascend_heaven_view_sign_up_rank()
        self.run_way.ascend_heaven.ascend_heaven_sign_up_rank()

    def run_cargo(self):
        #  镖行天下/获取之前的奖励-开始护送新的奖励
        self.run_way.cargo.cargo_get_info()
        self.run_way.cargo.cargo_transport_reward_complete()
        self.run_way.cargo.cargo_transport_receive_reward()
        # 开始护送新的奖励
        get_reward_info = self.run_way.cargo.cargo_get_reward_info()  # 获取奖励信息
        refresh_reward_times = self.run_way.cargo.cargo_get_refresh_reward_times()  # 获取刷新奖励次数
        if refresh_reward_times:
            for i in range(int(refresh_reward_times[0])):
                if self.run_way.cargo.Cargo.reward in get_reward_info:  # 刷到最好的奖励
                    self.run_way.cargo.cargo_transport_reward()  # 启程护送
                    break
                else:
                    self.run_way.cargo.cargo_refresh_reward()  # 刷新奖励
            self.run_way.cargo.cargo_transport_reward()  # 启程护送

    def run_challenge_boss_without_exp(self):
        # 帮派/boss乐斗
        for i in self.run_way.challenge_boss.ChallengeBoss.B_UID_WITHOUT_EXP:
            self.run_way.challenge_boss.challenge_boss(B_UID=i)

    def run_challenge_boss_exp(self):
        # 好友/boss乐斗
        for i in self.run_way.challenge_boss.ChallengeBoss.B_UID_EXP:
            self.run_way.challenge_boss.challenge_boss(B_UID=i)

    def run_daily_chest(self):
        # 每日宝箱/领取铜质-领取银质-领取金质
        self.run_way.daily_chest.daily_chest_copper()
        self.run_way.daily_chest.daily_chest_silver()
        self.run_way.daily_chest.daily_chest_gold()

    def run_daily_reward(self):
        # 每日奖励/领取
        for i in [self.run_way.daily_reward.DailyReward.key_login, self.run_way.daily_reward.DailyReward.key_meridian,
                  self.run_way.daily_reward.DailyReward.key_daren,
                  self.run_way.daily_reward.DailyReward.key_wu_zi_tian_shu]:
            self.run_way.daily_reward.daily_reward(key=i)

    def run_dragon_phoenix(self):
        # 龙凰论武每日领奖-赛季领奖
        self.run_way.dragon_phoenix.dragon_phoenix_gift()
        self.run_way.dragon_phoenix.dragon_phoenix_rank_reward()

    def run_dream_trip(self):
        # 梦想之旅/普通机票
        self.run_way.dream_trip.dream_trip()

    def run_fac_challenge(self):
        #  踢馆/领奖-试练-转盘-挑战
        import datetime
        reward_id = self.run_way.fac_challenge.fac_rank_reward_id()  # 排行奖励id查询
        self.run_way.fac_challenge.fac_rank_reward(subtype=int(reward_id[0])) if reward_id else None  # 排行奖励
        response = self.run_way.fac_challenge.fac_reward()  # 领奖
        time = f'{datetime.datetime.now().month}月{datetime.datetime.now().day}日'
        if time in response.raw_rsp.text:
            for i in range(5):
                self.run_way.fac_challenge.fac_practice()  # 试练
            self.run_way.fac_challenge.fac_table()  # 转盘
            for i in range(3):
                self.run_way.fac_challenge.fac_challenge()  # 挑战

    def run_fac_corp(self):
        # 帮派商会/查询会奖励-领取奖励
        gift_id = self.run_way.fac_corp.fac_corp_gift_id_exp()  # 查询会过期奖励id
        if gift_id:
            [self.run_way.fac_corp.fac_corp_gift(gift_id=int(n), type=self.run_way.fac_corp.FacCorp.type_exp) for n in
             gift_id]
        gift_id = self.run_way.fac_corp.fac_corp_gift_id_not_exp()  # 查询不会过期奖励id
        if gift_id:
            [self.run_way.fac_corp.fac_corp_gift(gift_id=int(n), type=self.run_way.fac_corp.FacCorp.type_not_exp) for n
             in
             gift_id]

    def run_fac_task(self):
        # 执行帮派任务-领取帮派任务奖励
        task_id_list = self.run_way.fac_task.fac_task_id()
        if task_id_list:
            task_id = list(dict.fromkeys(task_id_list))  # 去重
            for i in task_id:
                if int(i) in self.run_way.fac_task.FacTask.id.keys():
                    param = self.run_way.fac_task.FacTask.id.get(int(i))
                    self.run_way.fac_task.fac_perform_task(param)  # 执行帮派任务
                    self.run_way.fac_task.fac_reward(id=int(i))  # 领取帮派任务奖励

    def run_faction_army(self):
        # 帮派远征军/领取奖励-领取宝箱
        for i in range(self.run_way.faction_army.FactionArmy.point_id):
            self.run_way.faction_army.faction_army_point_award(point_id=i)
        for n in range(self.run_way.faction_army.FactionArmy.island_id):
            self.run_way.faction_army.faction_army_island_award(island_id=n)

    def run_faction_league(self):
        # 帮派黄金联赛/领取奖励
        get_id = self.run_way.faction_league.faction_league_get_id()
        self.run_way.faction_league.faction_league(op=int(get_id[0])) if get_id else None

    def run_faction_mine(self):
        # 矿洞/领取奖励-挑战
        self.run_way.faction_mine.faction_mine()
        for i in range(3):
            self.run_way.faction_mine.faction_fight()

    def run_forage_war(self):
        # 掠夺/领取奖励
        self.run_way.forage_war.forage_war()

    def run_immortals(self):
        # 仙武修真/领取80活跃度挑战次数/寻访/挑战
        self.run_way.immortals.immortals_get_reward()
        fight_times = self.run_way.immortals.immortals_get_fight_times()
        if fight_times and int(fight_times[0]) != 0:
            for i in range(int(fight_times[0])):
                self.run_way.immortals.immortals_visit()
                self.run_way.immortals.immortals_fight()

    def run_knight_arena(self):
        # 华山论剑/挑战
        for i in range(5):
            self.run_way.knight_arena.knight_arena()

    def run_luan_dou(self):
        # 全民乱斗奖励领取
        for i in range(15, 20):
            self.run_way.luan_dou.luan_dou_reward(id=i)

    def run_lucky_turn(self):
        # 幸运转盘
        response = self.run_way.lucky_turn.page_list().raw_rsp.text
        self.run_way.lucky_turn.lucky_turn() if self.run_way.lucky_turn.LuckyTurn.lucky_turn in response else None

    def run_map_push(self):
        # 历练/挑战
        for i in range(5):
            if i == 3 or i == 4:
                self.run_way.map_push.map_push_challenge(npcid=self.run_way.map_push.MapPush.npcid_next)
            else:
                self.run_way.map_push.map_push_challenge(npcid=self.run_way.map_push.MapPush.npcid)

    def run_menu_act(self):
        # 乐斗菜单/领取奖励
        response = self.run_way.menu_act.page_list().raw_rsp.text
        if self.run_way.menu_act.MenuAct.menu_act in response:
            [self.run_way.menu_act.menu_act(gift=i) for i in range(1, 6)]

    def run_misty(self):
        # 幻境/返回-进入-挑战
        self.run_way.misty.misty_return()
        misty_id = self.run_way.misty.misty_get_id()
        if misty_id:
            self.run_way.misty.misty_entry(stage_id=int(misty_id[-1]))
            [self.run_way.misty.misty_fight() for i in range(5)]

    def run_month_card(self):
        #  斗豆月卡/领取奖励
        self.run_way.month_card.month_card()

    def run_page_list(self):
        #  主页活动/领取奖励
        response = self.run_way.page_list.page_list().raw_rsp.text
        for k, v in self.run_way.page_list.Page.page_dict.items():
            if k in response and k == self.run_way.page_list.Page.page_list[0]:  # 乐斗菜单
                [self.run_way.page_list.page_list_get_reward(gift=i) for i in range(1, 6)]
            elif k in response and k == self.run_way.page_list.Page.page_list[1]:  # 登录有礼
                [self.run_way.page_list.page_list_get_reward(v, gift_index=i) for i in range(6, -1, -1)]
            elif k in response and k == self.run_way.page_list.Page.page_list[2]:  # 神魔转盘
                if self.run_way.page_list.Page.check_str in self.run_way.page_list.page_list_check(v[1]):
                    self.run_way.page_list.page_list_get_reward(v[0])
            elif k in response and k == self.run_way.page_list.Page.page_list[3]:  # 猜单双
                [self.run_way.page_list.page_list_get_reward(v) for i in range(6)]
            elif k in response and k == self.run_way.page_list.Page.page_list[4]:  # 开心娃娃机
                check_times = self.run_way.page_list.page_list_check_machine(v[1], re_exp=self.run_way.page_list.Page.check_times)
                if check_times and int(check_times[0]) == 1:
                    self.run_way.page_list.page_list_get_reward(v[0])
            elif k in response and k not in self.run_way.page_list.Page.page_list:
                self.run_way.page_list.page_list_get_reward(v)

    def run_recommend_manor(self):
        # 抢地盘/每日奖励
        self.run_way.recommend_manor.recommend_manor_reward()

    def run_scroll_dungeon(self):
        # 画卷迷踪/buff选择-挑战
        while True:
            gift_name = self.run_way.scroll_dungeon.ScrollDungeon.gift_name
            for i in range(1, 7):
                self.run_way.scroll_dungeon.scroll_dungeon_buff_chose(buff=i)
                response = self.run_way.scroll_dungeon.scroll_dungeon_fight(re_exp=gift_name, buff=i)
                if gift_name not in response:
                    break
            response = self.run_way.scroll_dungeon.scroll_dungeon_fight(re_exp=gift_name, buff=0)
            if gift_name not in response:
                break

    def run_sect(self):
        # 门派/进入木桩训练免费挑战-商店换战书-入同门切磋免费挑战-普通香炉-商店换香炉-高香香炉-挑战三个不同身份的boss-完成任务
        self.run_way.sect.sect_training_with_npc()  # 进入木桩训练免费挑战
        for i in range(3):
            response = self.run_way.sect.sect_training_with_member()  # 进入同门切磋免费挑战
            if self.run_way.sect.Sect.other_case in response.raw_rsp.text:
                self.run_way.sect.sect_exchange_letter()  # 商店换战书
        self.run_way.sect.sect_fumigate_free_incense()  # 普通香炉
        for i in range(2):
            response = self.run_way.sect.sect_fumigate_paid_incense()  # 高香香炉
            if self.run_way.sect.Sect.other_case_paid in response.raw_rsp.text:
                self.run_way.sect.sect_exchange_incense()  # 商店换香炉
        for i in range(1, 4):
            self.run_way.sect.sect_fumigate_challenge_boss(rank=i, pos=i)  # 挑战三个boss

        response = self.run_way.sect.sect_fumigate_task_id().raw_rsp.text  # 根据任务进入地方
        for k, v in self.run_way.sect.Sect.action_list.items():
            if k in response:
                self.run_way.sect.sect_fumigate_task_id(v)

        task_id = self.run_way.sect.sect_fumigate_task_id(re_exp=self.run_way.sect.Sect.complete_id)  # 查找已完成任务id
        if task_id:
            [self.run_way.sect.sect_fumigate_task_complete(task_id=int(n)) for n in task_id]   # 完成任务

    def run_sect_melee(self):
        # 会武/进入场地-挑战-冠军助威
        sect_melee_id = self.run_way.sect_melee.sect_melee_id()  # 获取场地id
        if sect_melee_id:
            for i in range(10):
                self.run_way.sect_melee.sect_melee_enter(scene=int(sect_melee_id[0]))  # 进入场地
                self.run_way.sect_melee.sect_melee_do_training()  # 挑战
        self.run_way.sect_melee.sect_melee_cheer()

    def run_sect_tournament(self):
        #  门派邀请赛/开始挑战
        self.run_way.sect_tournament.sect_tournament_signup()
        for i in range(5):
            self.run_way.sect_tournament.sect_tournament()

    def run_space_relic(self):
        # 时空遗迹/遗迹征伐/异兽洞窟/挑战-联合征伐-每周任务领取-赛季任务领取
        self.run_way.space_relic.space_relic_enter()
        self.run_way.space_relic.space_relic_enter_challenge()
        for i in range(1, 6):
            self.run_way.space_relic.space_relic_challenge(id=i)
        self.run_way.space_relic.space_relic_show_union()
        [self.run_way.space_relic.space_relic_week_task(id=i) for i in range(1, 4)]
        [self.run_way.space_relic.space_relic_season_task(id=i) for i in range(4, 9)]

    def run_t_battle(self):
        # 问鼎天下/领取奖励-资源领取-攻占已标记资源
        self.run_way.t_battle.t_battle_draw_reward()  # 领取奖励
        self.run_way.t_battle.t_battle_op_draw_release_reward()  # 资源奖励
        region_name = self.run_way.t_battle.t_battle_get_region_name()  # 区域名字
        region_id_list = self.run_way.t_battle.TBattle.region_id_list  # 区域id集合
        region_id = region_id_list.get(region_name[0]) if region_name else None  # 获取区域id
        re_exp_battle = fr'id=(\w+)&amp;region={region_id}">攻占'
        resource_id_list = self.run_way.t_battle.t_battle_get_resource_id(re_exp=re_exp_battle,
                                                                          region=region_id)  # 获取资源id集合
        resource_id = resource_id_list[-1] if resource_id_list else None  # 获取资源id
        self.run_way.t_battle.t_battle_occupy_region(id=resource_id, region=region_id)  # 攻占资源

    def run_ten_lottery(self):
        # 邪神秘宝/领取高级秘宝-领取极品秘宝
        self.run_way.ten_lottery.ten_lottery_high()
        self.run_way.ten_lottery.ten_lottery_best()

    def run_thrones_battle(self):
        # 群雄逐鹿/报名-领奖-排行榜领奖
        self.run_way.thrones_battle.thrones_battle_signup()
        self.run_way.thrones_battle.thrones_battle_enter()
        self.run_way.thrones_battle.thrones_battle_draw_reward()
        self.run_way.thrones_battle.thrones_battle_rank_draw_reward()

    def run_tower_fight(self):
        # 斗神塔/自动挑战-结束挑战
        self.run_way.tower_fight.tower_fight_auto()
        self.run_way.tower_fight.tower_fight_finish()

    def run_warrior_inn(self):
        # 侠士客栈/进入-领取奖励
        room_type = self.run_way.warrior_inn.warrior_inn_enter_get_type()
        if room_type:
            get_reward_times = self.run_way.warrior_inn.WarriorInn.num
            for i in range(get_reward_times):
                self.run_way.warrior_inn.warrior_inn_get_reward(type=int(room_type[0]), num=i + 1)

    def run_wl_mz(self):
        # 武林盟主/查看是否报名时间-报名-获取奖励-前往竞猜-选择玩家-确认
        get_id = self.run_way.wl_mz.wl_mz_view_get_id(re_exp=self.run_way.wl_mz.WlMz.get_id)
        self.run_way.wl_mz.wl_mz_get_award(section_id=int(get_id[0][0]), round_id=int(get_id[0][1])) if get_id else None  # 获取奖励
        response = self.run_way.wl_mz.wl_mz_view()  # 查看是否报名时间
        if self.run_way.wl_mz.WlMz.check_str in response.raw_rsp.text:
            self.run_way.wl_mz.wl_mz_sigh_up()  # 报名
        else:
            self.run_way.wl_mz.wl_mz_guess()  # 前往竞猜
            for i in range(self.run_way.wl_mz.WlMz.index):
                self.run_way.wl_mz.wl_mz_guess_up(index=i)  # 选择玩家
            self.run_way.wl_mz.wl_mz_confirm()  # 确认

    def run_wl_meeting(self):
        # 武林大会/报名
        self.run_way.wl_meeting.wl_meeting()

    def run_world_tree(self):
        # 世界树/进入/奇树灵鉴/福宝/一键领取经验-免费温养一次
        self.run_way.world_tree.world_tree_into()
        self.run_way.world_tree.world_tree_enter()
        self.run_way.world_tree.world_tree_fu_bao()
        self.run_way.world_tree.world_tree_auto_get()
        self.run_way.world_tree.world_tree_do_strengh(weapon_id=int(self.run_way.world_tree.get_weapon_id_back()[0]))

    def run_zodiac_dungeon(self):
        # 十二宫/双鱼宫普通扫荡
        self.run_way.zodiac_dungeon.zodiac_dungeon_normal()

    def run_without_exp(self):
        self.run_abyss_tide()
        self.run_arena()
        self.run_ascend_heaven()
        self.run_challenge_boss_without_exp()
        self.run_daily_chest()
        self.run_daily_reward()
        self.run_dragon_phoenix()
        self.run_dream_trip()
        self.run_fac_challenge()
        self.run_fac_corp()
        self.run_fac_task()
        self.run_faction_army()
        self.run_faction_league()
        self.run_faction_mine()
        self.run_forage_war()
        self.run_immortals()
        self.run_knight_arena()
        self.run_luan_dou()
        self.run_menu_act()
        self.run_misty()
        self.run_month_card()
        self.run_recommend_manor()
        self.run_sect()
        self.run_sect_melee()
        self.run_sect_tournament()
        self.run_space_relic()
        self.run_t_battle()
        self.run_ten_lottery()
        self.run_thrones_battle()
        self.run_warrior_inn()
        self.run_wl_mz()
        self.run_world_tree()
        self.run_zodiac_dungeon()
        self.run_altar()
        self.run_page_list()

    def run_exp(self):
        self.run_cargo()
        self.run_challenge_boss_exp()
        self.run_map_push()
        self.run_scroll_dungeon()
        self.run_tower_fight()
        self.run_wl_meeting()


if __name__ == '__main__':
    import time
    start_time = time.time()
    RunModel().run_without_exp()
    RunModel().run_exp()
    end_time = time.time()
    print(f'运行{round(end_time - start_time, 2)}s')
