import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
import json
import os
import threading
from run_model.all_model import RunModel


class AutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("游戏自动化控制面板")
        self.root.geometry("1000x700")
        self.run_model = RunModel()

        # 所有模块列表
        self.all_modules = [
            "龙凰之境", "世界树", "时空遗迹", "深渊之潮", "飞升大作战", "仙武修真",
            "侠士客栈", "全民乱斗", "武林盟主", "帮派黄金联赛", "帮派远征军", "帮派商会",
            "问鼎天下", "梦想之旅", "会武", "帮派祭坛", "门派邀请赛", "门派", "画卷迷踪",
            "群雄逐鹿", "幻境", "镖行天下", "任务", "斗神塔", "抢地盘", "十二宫", "竞技场",
            "踢馆", "掠夺", "矿洞", "斗豆月卡", "每日宝箱", "邪神秘宝", "华山论剑", "武林大会",
            "帮派任务", "每日奖励", "活动领奖"
        ]

        # 经验模块和非经验模块（示例分类，可根据实际情况调整）
        self.exp_modules = [
            "龙凰之境", "世界树", "时空遗迹", "深渊之潮", "仙武修真", "任务",
            "斗神塔", "十二宫", "竞技场", "矿洞", "帮派任务", "每日奖励"
        ]
        self.non_exp_modules = [m for m in self.all_modules if m not in self.exp_modules]

        # self.module_functions = {
        #     "深渊之潮": self.run_model.run_abyss_tide(),
        #     "帮派祭坛": self.run_model.run_altar(),
        #     "竞技场": self.run_model.run_arena(),
        #     "飞升大作战":self.run_model.run_ascend_heaven(),
        #     "镖行天下": self.run_model.run_cargo(),
        #     "帮派侠侣boss乐斗": self.run_model.run_challenge_boss_without_exp(),
        #     "好友boss乐斗": self.run_model.run_challenge_boss_exp(),
        #     "每日宝箱": self.run_model.run_daily_chest(),
        #     "每日奖励": self.run_model.run_daily_reward(),
        #     "龙凰论武": self.run_model.run_dragon_phoenix(),
        #     "梦想之旅": self.run_model.run_dream_trip(),
        #     "踢馆": self.run_model.run_fac_challenge(),
        #     "帮派商会": self.run_model.run_fac_corp(),
        #     "执行帮派任务": self.run_model.run_fac_task(),
        #     "帮派远征军": self.run_model.run_faction_army(),
        #     "帮派黄金联赛": self.run_model.run_faction_league(),
        #     "矿洞": self.run_model.run_faction_mine(),
        #     "掠夺": self.run_model.run_forage_war(),
        #     "仙武修真": self.run_model.run_immortals(),
        #     "华山论剑": self.run_model.run_knight_arena(),
        #     "全民乱斗": self.run_model.run_luan_dou(),
        #     "幸运转盘": self.run_model.run_lucky_turn(),
        #     "历练": self.run_model.run_map_push(),
        #     "乐斗菜单": self.run_model.run_menu_act(),
        #     "幻境": self.run_model.run_misty(),
        #     "斗豆月卡": self.run_model.run_month_card(),
        #     "抢地盘": self.run_model.run_recommend_manor(),
        #     "画卷迷踪": self.run_model.run_scroll_dungeon(),
        #     "门派": self.run_model.run_sect(),
        #     "会武": self.run_model.run_sect_melee(),
        #     "门派邀请赛": self.run_model.run_sect_tournament(),
        #     "时空遗迹": self.run_model.run_space_relic(),
        #     "问鼎天下": self.run_model.run_t_battle(),
        #     "邪神秘宝": self.run_model.run_ten_lottery(),
        #     "群雄逐鹿": self.run_model.run_thrones_battle(),
        #     "斗神塔": self.run_model.run_tower_fight(),
        #     "侠士客栈": self.run_model.run_warrior_inn(),
        #     "武林盟主": self.run_model.run_wl_mz(),
        #     "武林大会": self.run_model.run_wl_meeting(),
        #     "世界树": self.run_model.run_world_tree(),
        #     "十二宫": self.run_model.run_zodiac_dungeon()
        # }

        # 配置文件路径
        self.config_file = "config.json"
        self.accounts_file = "accounts.json"

        # 初始化配置
        self.load_config()
        self.load_accounts()

        # 创建界面
        self.create_widgets()

        # 初始化执行状态
        self.is_running = False
        self.current_thread = None

    def load_config(self):
        """加载配置文件"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    self.config = json.load(f)
            else:
                self.config = {"settings": {}}
        except:
            self.config = {"settings": {}}

    def save_config(self):
        """保存配置文件"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=4, ensure_ascii=False)

    def load_accounts(self):
        """加载账号列表"""
        try:
            if os.path.exists(self.accounts_file):
                with open(self.accounts_file, 'r', encoding='utf-8') as f:
                    self.accounts = json.load(f)
            else:
                self.accounts = []
        except:
            self.accounts = []

    def save_accounts(self):
        """保存账号列表"""
        with open(self.accounts_file, 'w', encoding='utf-8') as f:
            json.dump(self.accounts, f, indent=4, ensure_ascii=False)

    def create_widgets(self):
        """创建界面组件"""
        # 创建主框架
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 创建顶部按钮区域
        top_frame = ttk.Frame(main_frame)
        top_frame.pack(fill=tk.X, pady=(0, 10))

        # 一键执行按钮
        self.run_all_btn = ttk.Button(
            top_frame,
            text="一键执行全部",
            command=lambda: self.run_modules(self.all_modules)
        )
        self.run_all_btn.pack(side=tk.LEFT, padx=5)

        # 执行经验模块按钮
        self.run_exp_btn = ttk.Button(
            top_frame,
            text="执行经验模块",
            command=lambda: self.run_modules(self.exp_modules)
        )
        self.run_exp_btn.pack(side=tk.LEFT, padx=5)

        # 执行非经验模块按钮
        self.run_non_exp_btn = ttk.Button(
            top_frame,
            text="执行非经验模块",
            command=lambda: self.run_modules(self.non_exp_modules)
        )
        self.run_non_exp_btn.pack(side=tk.LEFT, padx=5)

        # 配置按钮
        self.config_btn = ttk.Button(
            top_frame,
            text="配置",
            command=self.open_config_window
        )
        self.config_btn.pack(side=tk.RIGHT, padx=5)

        # 账号管理按钮
        self.account_btn = ttk.Button(
            top_frame,
            text="账号管理",
            command=self.open_account_window
        )
        self.account_btn.pack(side=tk.RIGHT, padx=5)

        # 创建模块选择区域
        module_frame = ttk.LabelFrame(main_frame, text="模块选择")
        module_frame.pack(fill=tk.BOTH, expand=True)

        # 创建模块选择树状视图
        self.module_tree = ttk.Treeview(module_frame, selectmode="extended")
        self.module_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # 添加列
        self.module_tree["columns"] = ("status", "time")
        self.module_tree.column("#0", width=200, minwidth=100)
        self.module_tree.column("status", width=100, minwidth=50, anchor="center")
        self.module_tree.column("time", width=100, minwidth=50, anchor="center")

        # 添加表头
        self.module_tree.heading("#0", text="模块名称", anchor="w")
        self.module_tree.heading("status", text="状态", anchor="center")
        self.module_tree.heading("time", text="耗时", anchor="center")

        # 添加模块到树状视图
        for module in self.all_modules:
            self.module_tree.insert("", "end", text=module, values=("未执行", "-"))

        # 创建底部按钮区域
        bottom_frame = ttk.Frame(main_frame)
        bottom_frame.pack(fill=tk.X, pady=(10, 0))

        # 执行选中模块按钮
        self.run_selected_btn = ttk.Button(
            bottom_frame,
            text="执行选中模块",
            command=self.run_selected_modules
        )
        self.run_selected_btn.pack(side=tk.LEFT, padx=5)

        # 停止执行按钮
        self.stop_btn = ttk.Button(
            bottom_frame,
            text="停止执行",
            command=self.stop_execution,
            state=tk.DISABLED
        )
        self.stop_btn.pack(side=tk.LEFT, padx=5)

        # 日志区域
        log_frame = ttk.LabelFrame(main_frame, text="执行日志")
        log_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))

        self.log_text = tk.Text(log_frame, height=10)
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # 添加滚动条
        scrollbar = ttk.Scrollbar(self.log_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.log_text.yview)

        # 初始化执行状态
        self.is_running = False
        self.current_thread = None

    def run_modules(self, modules):
        """执行指定模块"""
        if self.is_running:
            messagebox.showwarning("警告", "已有任务正在执行，请等待完成或停止当前任务")
            return

        if not modules:
            messagebox.showinfo("提示", "没有可执行的模块")
            return

        # 更新UI状态
        self.is_running = True
        self.stop_btn.config(state=tk.NORMAL)
        self.run_all_btn.config(state=tk.DISABLED)
        self.run_exp_btn.config(state=tk.DISABLED)
        self.run_non_exp_btn.config(state=tk.DISABLED)
        self.run_selected_btn.config(state=tk.DISABLED)
        self.config_btn.config(state=tk.DISABLED)
        self.account_btn.config(state=tk.DISABLED)

        # 清空日志
        self.log_text.delete(1.0, tk.END)
        self.add_log(f"开始执行 {len(modules)} 个模块...")

        # 在新线程中执行模块
        self.current_thread = threading.Thread(
            target=self._execute_modules,
            args=(modules,),
            daemon=True
        )
        self.current_thread.start()

    def _execute_modules(self, modules):
        """实际执行模块的函数"""
        try:
            for module in modules:
                if not self.is_running:
                    break

                # 更新模块状态为"执行中"
                self.update_module_status(module, "执行中", "-")
                self.add_log(f"开始执行模块: {module}")

                # 模拟执行模块（实际使用时替换为您的模块执行代码）
                import time
                time.sleep(1)  # 模拟执行时间

                # 随机模拟成功或失败
                import random
                if random.random() > 0.2:  # 80%成功率
                    status = "完成"
                    time_used = f"{random.randint(1, 30)}秒"
                    self.add_log(f"模块 {module} 执行成功，耗时 {time_used}")
                else:
                    status = "失败"
                    time_used = f"{random.randint(1, 10)}秒"
                    self.add_log(f"模块 {module} 执行失败，耗时 {time_used}")

                # 更新模块状态
                self.update_module_status(module, status, time_used)

            self.add_log("所有模块执行完成" if self.is_running else "执行已停止")
        except Exception as e:
            self.add_log(f"执行出错: {str(e)}")
        finally:
            # 恢复UI状态
            self.root.after(0, self._reset_ui)

    def _reset_ui(self):
        """重置UI状态"""
        self.is_running = False
        self.stop_btn.config(state=tk.DISABLED)
        self.run_all_btn.config(state=tk.NORMAL)
        self.run_exp_btn.config(state=tk.NORMAL)
        self.run_non_exp_btn.config(state=tk.NORMAL)
        self.run_selected_btn.config(state=tk.NORMAL)
        self.config_btn.config(state=tk.NORMAL)
        self.account_btn.config(state=tk.NORMAL)

    def run_selected_modules(self):
        """执行选中的模块"""
        selected_items = self.module_tree.selection()
        if not selected_items:
            messagebox.showinfo("提示", "请先选择要执行的模块")
            return
        # 获取选中的模块名称
        selected_modules = [self.module_tree.item(item, "text") for item in selected_items]
        # 执行选中的模块
        self.run_modules(selected_modules)

    def stop_execution(self):
        """停止执行"""
        if self.is_running:
            self.is_running = False
            self.add_log("正在停止执行...")
            self.stop_btn.config(state=tk.DISABLED)

    def update_module_status(self, module, status, time_used):
        """更新模块状态"""
        for item in self.module_tree.get_children():
            if self.module_tree.item(item, "text") == module:
                self.module_tree.item(item, values=(status, time_used))
                self.module_tree.update()
                break

    def add_log(self, message):
        """添加日志"""
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.update()

    def open_config_window(self):
        """打开配置窗口"""
        config_window = tk.Toplevel(self.root)
        config_window.title("配置设置")
        config_window.geometry("600x400")

        # 创建配置编辑区域
        config_frame = ttk.Frame(config_window)
        config_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 配置文本编辑框
        config_label = ttk.Label(config_frame, text="配置文件内容:")
        config_label.pack(anchor="w")

        self.config_text = tk.Text(config_frame, height=15)
        self.config_text.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        # 加载当前配置
        config_str = json.dumps(self.config, indent=4, ensure_ascii=False)
        self.config_text.insert(tk.END, config_str)

        # 按钮区域
        button_frame = ttk.Frame(config_frame)
        button_frame.pack(fill=tk.X, pady=(10, 0))

        # 保存按钮
        save_btn = ttk.Button(
            button_frame,
            text="保存配置",
            command=lambda: self.save_config_from_window(config_window)
        )
        save_btn.pack(side=tk.LEFT, padx=5)

        # 取消按钮
        cancel_btn = ttk.Button(
            button_frame,
            text="取消",
            command=config_window.destroy
        )
        cancel_btn.pack(side=tk.RIGHT, padx=5)

    def save_config_from_window(self, window):
        """从配置窗口保存配置"""
        try:
            new_config = json.loads(self.config_text.get("1.0", tk.END))
            self.config = new_config
            self.save_config()
            messagebox.showinfo("成功", "配置已保存并生效")
            window.destroy()
        except json.JSONDecodeError as e:
            messagebox.showerror("错误", f"配置格式错误: {str(e)}")

    def open_account_window(self):
        """打开账号管理窗口"""
        account_window = tk.Toplevel(self.root)
        account_window.title("账号管理")
        account_window.geometry("800x500")

        # 创建账号列表区域
        account_frame = ttk.Frame(account_window)
        account_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 账号列表树状视图
        self.account_tree = ttk.Treeview(account_frame)
        self.account_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # 添加列
        self.account_tree["columns"] = ("username", "status", "last_run")
        self.account_tree.column("#0", width=50, minwidth=50)
        self.account_tree.column("username", width=150, minwidth=100)
        self.account_tree.column("status", width=100, minwidth=80)
        self.account_tree.column("last_run", width=150, minwidth=100)

        # 添加表头
        self.account_tree.heading("#0", text="序号", anchor="w")
        self.account_tree.heading("username", text="用户名", anchor="w")
        self.account_tree.heading("status", text="状态", anchor="center")
        self.account_tree.heading("last_run", text="最后执行时间", anchor="center")

        # 加载账号列表
        self.refresh_account_tree()

        # 按钮区域
        button_frame = ttk.Frame(account_frame)
        button_frame.pack(fill=tk.X, pady=(10, 0))

        # 添加账号按钮
        add_btn = ttk.Button(
            button_frame,
            text="添加账号",
            command=self.add_account
        )
        add_btn.pack(side=tk.LEFT, padx=5)

        # 删除账号按钮
        delete_btn = ttk.Button(
            button_frame,
            text="删除账号",
            command=self.delete_account
        )
        delete_btn.pack(side=tk.LEFT, padx=5)

        # 编辑账号按钮
        edit_btn = ttk.Button(
            button_frame,
            text="编辑账号",
            command=self.edit_account
        )
        edit_btn.pack(side=tk.LEFT, padx=5)

        # 运行选中账号按钮
        run_btn = ttk.Button(
            button_frame,
            text="运行选中账号",
            command=self.run_selected_accounts
        )
        run_btn.pack(side=tk.RIGHT, padx=5)

        # 关闭按钮
        close_btn = ttk.Button(
            button_frame,
            text="关闭",
            command=account_window.destroy
        )
        close_btn.pack(side=tk.RIGHT, padx=5)

    def refresh_account_tree(self):
        """刷新账号列表"""
        # 清空现有数据
        for item in self.account_tree.get_children():
            self.account_tree.delete(item)

        # 添加账号数据
        for i, account in enumerate(self.accounts, 1):
            self.account_tree.insert(
                "", "end",
                text=str(i),
                values=(
                    account.get("username", ""),
                    account.get("status", "未运行"),
                    account.get("last_run", "-")
                )
            )

    def add_account(self):
        """添加新账号"""
        username = simpledialog.askstring("添加账号", "请输入用户名:")
        if username:
            password = simpledialog.askstring("添加账号", "请输入密码:", show="*")
            if password:
                new_account = {
                    "username": username,
                    "password": password,
                    "status": "未运行",
                    "last_run": "-"
                }
                self.accounts.append(new_account)
                self.save_accounts()
                self.refresh_account_tree()
                messagebox.showinfo("成功", "账号添加成功")

    def delete_account(self):
        """删除选中账号"""
        selected_items = self.account_tree.selection()
        if not selected_items:
            messagebox.showinfo("提示", "请先选择要删除的账号")
            return

        # 确认删除
        if messagebox.askyesno("确认", "确定要删除选中的账号吗？"):
            # 从后往前删除以避免索引问题
            for item in reversed(selected_items):
                index = int(self.account_tree.item(item, "text")) - 1
                if 0 <= index < len(self.accounts):
                    del self.accounts[index]

            self.save_accounts()
            self.refresh_account_tree()
            messagebox.showinfo("成功", "账号删除成功")

    def edit_account(self):
        """编辑选中账号"""
        selected_items = self.account_tree.selection()
        if not selected_items or len(selected_items) > 1:
            messagebox.showinfo("提示", "请选择要编辑的一个账号")
            return

        item = selected_items[0]
        index = int(self.account_tree.item(item, "text")) - 1
        if 0 <= index < len(self.accounts):
            account = self.accounts[index]

            edit_window = tk.Toplevel(self.root)
            edit_window.title("编辑账号")
            edit_window.geometry("400x300")

            # 用户名
            ttk.Label(edit_window, text="用户名:").pack(pady=(10, 0))
            username_entry = ttk.Entry(edit_window)
            username_entry.pack(fill=tk.X, padx=20, pady=(0, 10))
            username_entry.insert(0, account["username"])

            # 密码
            ttk.Label(edit_window, text="密码:").pack()
            password_entry = ttk.Entry(edit_window, show="*")
            password_entry.pack(fill=tk.X, padx=20, pady=(0, 20))
            password_entry.insert(0, account["password"])

            # 保存按钮
            def save_changes():
                account["username"] = username_entry.get()
                account["password"] = password_entry.get()
                self.save_accounts()
                self.refresh_account_tree()
                edit_window.destroy()
                messagebox.showinfo("成功", "账号信息已更新")

            ttk.Button(
                edit_window,
                text="保存",
                command=save_changes
            ).pack(pady=10)

    def run_selected_accounts(self):
        """运行选中账号"""
        selected_items = self.account_tree.selection()
        if not selected_items:
            messagebox.showinfo("提示", "请先选择要运行的账号")
            return

        selected_accounts = []
        for item in selected_items:
            index = int(self.account_tree.item(item, "text")) - 1
            if 0 <= index < len(self.accounts):
                selected_accounts.append(self.accounts[index])

        if not selected_accounts:
            return

        # 确认运行
        if messagebox.askyesno("确认", f"确定要运行选中的 {len(selected_accounts)} 个账号吗？"):
            self.add_log(f"开始运行 {len(selected_accounts)} 个账号...")

            # 在新线程中运行账号
            threading.Thread(
                target=self._execute_accounts,
                args=(selected_accounts,),
                daemon=True
            ).start()

    def _execute_accounts(self, accounts):
        """实际执行账号的函数"""
        try:
            for account in accounts:
                if not self.is_running:
                    break

                username = account["username"]
                self.add_log(f"开始运行账号: {username}")

                # 更新账号状态
                self._update_account_status(username, "运行中", "-")

                # 模拟执行（实际使用时替换为您的账号执行代码）
                import time
                time.sleep(2)  # 模拟执行时间

                # 随机模拟成功或失败
                import random
                if random.random() > 0.2:  # 80%成功率
                    status = "完成"
                    last_run = time.strftime("%Y-%m-%d %H:%M:%S")
                    self.add_log(f"账号 {username} 运行成功")
                else:
                    status = "失败"
                    last_run = time.strftime("%Y-%m-%d %H:%M:%S")
                    self.add_log(f"账号 {username} 运行失败")

                # 更新账号状态
                self._update_account_status(username, status, last_run)

            self.add_log("所有账号运行完成" if self.is_running else "运行已停止")
        except Exception as e:
            self.add_log(f"运行出错: {str(e)}")

    def _update_account_status(self, username, status, last_run):
        """更新账号状态"""
        for i, account in enumerate(self.accounts):
            if account["username"] == username:
                account["status"] = status
                account["last_run"] = last_run
                self.save_accounts()

                # 更新UI
                self.root.after(0, lambda: self.refresh_account_tree())
                break


if __name__ == "__main__":
    root = tk.Tk()
    app = AutomationApp(root)
    root.mainloop()
