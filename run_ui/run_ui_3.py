import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from public_common.get_cookie import GetCookie
import os
import threading
import time
import sys
from io import StringIO
from run_model.all_model import RunModel
from public_common.log import logger
from public_common.log import log_path
import logging
from logging.handlers import QueueHandler
import queue


class AutomationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("游戏自动化控制面板")
        self.root.geometry("1000x700")
        self.run_model = RunModel()

        # 设置日志系统
        self.setup_logging()

        # 重定向标准输出
        self.original_stdout = sys.stdout
        self.output_buffer = StringIO()
        sys.stdout = self.output_buffer

        # 配置文件路径
        self.config_dir = os.path.join(os.path.dirname(log_path), 'config')
        self.config_file =os.path.join(self.config_dir, 'config.ini')

        # 确保配置目录存在
        os.makedirs(self.config_dir, exist_ok=True)

        # 初始化配置
        self.load_config()

        # 模块函数映射
        self.module_functions = {
            "深渊之潮": self.run_model.run_abyss_tide,
            "竞技场": self.run_model.run_arena,
            "飞升大作战": self.run_model.run_ascend_heaven,
            "镖行天下": self.run_model.run_cargo,
            '帮派boss乐斗': self.run_model.run_challenge_boss_without_exp,
            "好友boss乐斗": self.run_model.run_challenge_boss_exp,
            "每日宝箱": self.run_model.run_daily_chest,
            "每日奖励": self.run_model.run_daily_reward,
            "龙凰论武": self.run_model.run_dragon_phoenix,
            "梦想之旅": self.run_model.run_dream_trip,
            "踢馆": self.run_model.run_fac_challenge,
            "帮派商会": self.run_model.run_fac_corp,
            "执行帮派任务": self.run_model.run_fac_task,
            "帮派远征军": self.run_model.run_faction_army,
            "帮派黄金联赛": self.run_model.run_faction_league,
            "矿洞": self.run_model.run_faction_mine,
            "掠夺": self.run_model.run_forage_war,
            "仙武修真": self.run_model.run_immortals,
            "华山论剑": self.run_model.run_knight_arena,
            "历练": self.run_model.run_map_push,
            "幻境": self.run_model.run_misty,
            "斗豆月卡": self.run_model.run_month_card,
            "抢地盘": self.run_model.run_recommend_manor,
            "画卷迷踪": self.run_model.run_scroll_dungeon,
            "门派": self.run_model.run_sect,
            "会武": self.run_model.run_sect_melee,
            "全民乱斗": self.run_model.run_luan_dou,
            "门派邀请赛": self.run_model.run_sect_tournament,
            "时空遗迹": self.run_model.run_space_relic,
            "问鼎天下": self.run_model.run_t_battle,
            "邪神秘宝": self.run_model.run_ten_lottery,
            "群雄逐鹿": self.run_model.run_thrones_battle,
            "斗神塔": self.run_model.run_tower_fight,
            "侠士客栈": self.run_model.run_warrior_inn,
            "武林盟主": self.run_model.run_wl_mz,
            "武林大会": self.run_model.run_wl_meeting,
            "世界树": self.run_model.run_world_tree,
            "十二宫": self.run_model.run_zodiac_dungeon,
            "帮派祭坛": self.run_model.run_altar,
            "主页活动": self.run_model.run_page_list
        }

        # 经验模块列表
        self.exp_modules = [
            "镖行天下", "好友boss乐斗", "历练",
            "画卷迷踪", "斗神塔", "武林大会"
        ]

        # 创建界面
        self.create_widgets()

        # 初始化执行状态
        self.is_running = False
        self.current_thread = None

    def setup_logging(self):
        """配置日志系统以捕获模块日志"""
        # 创建日志队列
        self.log_queue = queue.Queue()

        # 使用导入的logger
        global logger
        logger.setLevel(logging.INFO)

        # 添加队列处理器
        queue_handler = QueueHandler(self.log_queue)
        logger.addHandler(queue_handler)

        # 防止日志传播到根logger
        logger.propagate = False

        # 启动日志监听线程
        self.log_listener = threading.Thread(
            target=self.process_log_queue,
            daemon=True
        )
        self.log_listener.start()

    def process_log_queue(self):
        """处理日志队列中的消息"""
        while True:
            try:
                record = self.log_queue.get()
                if record is None:  # 终止信号
                    break

                msg = self.format_log_record(record)
                self.root.after(0, self.add_log, msg)
            except Exception:
                break

    def format_log_record(self, record):
        """格式化日志记录"""
        # 移除可能已存在的时间戳
        message = record.getMessage()
        if message.startswith('[') and ']' in message:
            message = message.split(']', 1)[1].strip()
        return f"[{time.strftime('%H:%M:%S')}] {message}"

    def __del__(self):
        """清理资源"""
        # 发送终止信号到日志队列
        self.log_queue.put(None)
        if hasattr(self, 'log_listener'):
            self.log_listener.join(timeout=1)
        # 恢复标准输出
        sys.stdout = self.original_stdout

    # --------------------------
    # 配置文件管理
    # --------------------------
    def load_config(self):
        """加载配置文件"""
        self.config = GetCookie().get_cookie()
        if os.path.exists(self.config_file):
            self.config.read(self.config_file, encoding='utf-8')
        else:
            # 默认配置
            self.config['qq_num'] = {
                'run_qq_num': '1',
                'abyss_tide_enter': '2',
                'ascend_heaven': '2'
            }
            self.config['qq_cookie'] = {
                'qq_num_1': 'openId=xxx; accessToken=xxx; newuin=xxx'
            }
            self.save_config()

    def save_config(self):
        """保存配置文件"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            self.config.write(f)

    # --------------------------
    # UI界面
    # --------------------------
    def create_widgets(self):
        """创建主界面"""
        # 主框架
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 顶部按钮区域
        top_frame = ttk.Frame(main_frame)
        top_frame.pack(fill=tk.X, pady=(0, 10))

        # 按照要求的顺序排列按钮
        ttk.Button(
            top_frame, text="执行选中模块",
            command=self.run_selected_modules
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            top_frame, text="执行非经验模块",
            command=self.run_non_exp_modules
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            top_frame, text="执行经验模块",
            command=lambda: self.run_modules(self.exp_modules)
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            top_frame, text="一键运行全部",
            command=self.run_all_modules
        ).pack(side=tk.LEFT, padx=5)

        # 停止按钮
        self.stop_btn = ttk.Button(
            top_frame, text="停止执行",
            command=self.stop_execution,
            state=tk.DISABLED
        )
        self.stop_btn.pack(side=tk.LEFT, padx=5)

        # 配置按钮
        ttk.Button(
            top_frame, text="配置管理",
            command=self.open_config_window
        ).pack(side=tk.RIGHT, padx=5)

        # 模块选择区域
        module_frame = ttk.LabelFrame(main_frame, text="模块选择")
        module_frame.pack(fill=tk.BOTH, expand=True)

        # 模块树状列表
        self.module_tree = ttk.Treeview(
            module_frame,
            columns=("status", "time"),
            selectmode="extended",
            height=15
        )
        self.module_tree.pack(fill=tk.BOTH, expand=True)

        # 设置列
        self.module_tree.column("#0", width=200, minwidth=150, anchor="center")
        self.module_tree.column("status", width=100, anchor="center")
        self.module_tree.column("time", width=100, anchor="center")

        # 设置表头
        self.module_tree.heading("#0", text="模块名称")
        self.module_tree.heading("status", text="状态")
        self.module_tree.heading("time", text="耗时")

        # 添加模块到树状视图
        for module in self.module_functions.keys():
            self.module_tree.insert("", "end", text=module, values=("未执行", "-"))

        # 日志区域
        log_frame = ttk.LabelFrame(main_frame, text="执行日志")
        log_frame.pack(fill=tk.BOTH, expand=True, pady=(10, 0))

        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            wrap=tk.WORD,
            height=10
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)

    # --------------------------
    # 核心功能
    # --------------------------
    def run_all_modules(self):
        """执行所有模块"""
        all_modules = list(self.module_functions.keys())
        self.run_modules(all_modules)

    def run_non_exp_modules(self):
        """执行非经验模块"""
        non_exp_modules = [module for module in self.module_functions.keys()
                           if module not in self.exp_modules]
        self.run_modules(non_exp_modules)

    def run_selected_modules(self):
        """执行选中的模块"""
        selected_items = self.module_tree.selection()
        if not selected_items:
            messagebox.showinfo("提示", "请先选择要执行的模块")
            return

        selected_modules = [self.module_tree.item(item, "text") for item in selected_items]
        self.run_modules(selected_modules)

    def run_modules(self, modules):
        """执行指定模块列表"""
        if self.is_running:
            messagebox.showwarning("警告", "已有任务正在执行")
            return

        self.is_running = True
        self.stop_btn.config(state=tk.NORMAL)
        self.log_text.delete(1.0, tk.END)
        self.add_log(f"开始执行 {len(modules)} 个模块...")

        # 在新线程中执行
        self.current_thread = threading.Thread(
            target=self._execute_modules,
            args=(modules,),
            daemon=True
        )
        self.current_thread.start()

    def _execute_modules(self, modules):
        """实际执行模块"""
        try:
            for module in modules:
                if not self.is_running:
                    break

                # 更新状态
                self.update_module_status(module, "执行中", "-")
                self.add_log(f"开始执行: {module}")

                # 获取并执行模块函数
                module_func = self.module_functions.get(module)
                if module_func:
                    try:
                        # 记录开始时间并执行
                        start_time = time.time()
                        module_func()  # 不再接收返回值
                        elapsed = time.time() - start_time

                        # 更新状态为完成
                        status = "完成"
                        time_used = f"{elapsed:.2f}s"

                        self.add_log(f"{module} 执行完成，耗时 {time_used}")
                    except Exception as e:
                        status = "错误"
                        time_used = "-"
                        self.add_log(f"{module} 执行出错: {str(e)}")
                else:
                    status = "未实现"
                    time_used = "-"
                    self.add_log(f"{module} 功能未实现")

                # 更新UI状态
                self.update_module_status(module, status, time_used)

            self.add_log("模块执行完成" if self.is_running else "执行已停止")
        except Exception as e:
            self.add_log(f"执行过程出错: {str(e)}")
        finally:
            self.root.after(0, self._reset_ui)

    def stop_execution(self):
        """停止执行"""
        if self.is_running:
            self.is_running = False
            self.add_log("正在停止执行...")
            self.stop_btn.config(state=tk.DISABLED)

    def _reset_ui(self):
        """重置UI状态"""
        self.is_running = False
        self.stop_btn.config(state=tk.DISABLED)

    def update_module_status(self, module, status, time_used):
        """更新模块状态"""
        for item in self.module_tree.get_children():
            if self.module_tree.item(item, "text") == module:
                self.module_tree.item(item, values=(status, time_used))
                break

    def add_log(self, message):
        """添加日志"""
        timestamp = time.strftime("%H:%M:%S", time.localtime())
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_text.see(tk.END)
        self.log_text.update()

    # --------------------------
    # 配置管理窗口
    # --------------------------
    def open_config_window(self):
        """打开配置编辑窗口"""
        config_window = tk.Toplevel(self.root)
        config_window.title("配置管理")
        config_window.geometry("600x500")

        # 使配置窗口置顶
        config_window.grab_set()
        config_window.focus_set()

        # 配置编辑区域
        config_frame = ttk.Frame(config_window)
        config_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 文本编辑框
        self.config_text = scrolledtext.ScrolledText(
            config_frame,
            wrap=tk.WORD,
            font=('Consolas', 10)
        )
        self.config_text.pack(fill=tk.BOTH, expand=True)

        # 直接加载配置文件原始内容
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                config_content = f.read()
                self.config_text.insert(tk.END, config_content)
        except Exception as e:
            messagebox.showerror("错误", f"无法读取配置文件: {str(e)}")

        # 按钮区域
        btn_frame = ttk.Frame(config_frame)
        btn_frame.pack(fill=tk.X, pady=(10, 0))

        ttk.Button(
            btn_frame, text="保存配置",
            command=lambda: self.save_config_from_window(config_window)
        ).pack(side=tk.LEFT, padx=5)

        ttk.Button(
            btn_frame, text="取消",
            command=config_window.destroy
        ).pack(side=tk.RIGHT, padx=5)

    def save_config_from_window(self, window):
        """从窗口保存配置并立即生效"""
        try:
            # 直接保存文本内容
            with open(self.config_file, 'w', encoding='utf-8') as f:
                f.write(self.config_text.get("1.0", tk.END))

            # 重新加载配置
            self.load_config()

            # 更新运行时配置
            self.update_runtime_config()

            messagebox.showinfo("成功", "配置已保存并生效")
            window.destroy()
        except Exception as e:
            messagebox.showerror("错误", f"保存配置失败: {str(e)}")

    def update_runtime_config(self):
        """更新运行时配置"""
        # 更新RunModel中的配置
        if hasattr(self.run_model, 'update_config'):
            self.run_model.update_config(self.config)


if __name__ == "__main__":
    root = tk.Tk()
    app = AutomationApp(root)
    root.mainloop()
