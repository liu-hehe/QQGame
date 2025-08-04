import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk
import io
import threading
import time
import re
import urllib.parse
import json
from pathlib import Path


class QQLoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QQ扫码登录")
        self.root.geometry("400x550")

        # 文件保存路径
        self.cookie_file = Path("D:/qq_game/run_ui/cookie.json")

        # 使用已验证可工作的URL
        self.appid = "716027609"
        self.ptqrshow_url = "https://ssl.ptlogin2.qq.com/ptqrshow"
        self.ptqrlogin_url = "https://ssl.ptlogin2.qq.com/ptqrlogin"
        self.redirect_uri = urllib.parse.quote("https://graph.qq.com/oauth2.0/login_jump")

        # 登录状态
        self.qrsig = ""
        self.login_status = False

        self.create_widgets()
        self.refresh_qrcode()

    def create_widgets(self):
        """创建界面组件"""
        # 标题
        title_label = ttk.Label(self.root, text="QQ扫码登录", font=('微软雅黑', 16))
        title_label.pack(pady=15)

        # 二维码显示区域
        self.qr_frame = ttk.Frame(self.root)
        self.qr_frame.pack()

        self.qr_label = ttk.Label(self.qr_frame)
        self.qr_label.pack()

        # 状态显示
        self.status_var = tk.StringVar()
        self.status_var.set("正在获取二维码...")
        self.status_label = ttk.Label(self.root, textvariable=self.status_var,
                                      font=('微软雅黑', 12), foreground="blue")
        self.status_label.pack(pady=10)

        # 刷新按钮
        refresh_btn = ttk.Button(self.root, text="刷新二维码", command=self.refresh_qrcode)
        refresh_btn.pack(pady=10)

    def refresh_qrcode(self):
        """获取并显示QQ登录二维码"""
        self.status_var.set("正在获取二维码...")
        self.login_status = False

        try:
            # 使用已验证的请求头和参数
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Referer": "https://xui.ptlogin2.qq.com/"
            }

            params = {
                "appid": self.appid,
                "e": "2",
                "l": "M",
                "s": "3",
                "d": "72",
                "v": "4",
                "t": str(time.time()),
                "daid": "383",
                "pt_3rd_aid": "0"
            }

            response = requests.get(self.ptqrshow_url, params=params, headers=headers)

            # 验证响应内容
            if 'image/' not in response.headers.get('Content-Type', ''):
                raise ValueError("响应不是图片，可能接口已变更")

            # 获取qrsig
            self.qrsig = response.cookies.get('qrsig', '')
            if not self.qrsig:
                raise ValueError("未能获取qrsig")

            # 显示二维码
            img = Image.open(io.BytesIO(response.content))
            img = img.resize((250, 250), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)

            self.qr_label.config(image=img_tk)
            self.qr_label.image = img_tk

            self.status_var.set("请使用手机QQ扫码")

            # 开始轮询登录状态
            threading.Thread(target=self.poll_login_status, daemon=True).start()

        except Exception as e:
            self.status_var.set(f"获取二维码失败: {str(e)}")
            print(f"错误详情: {e}")
            messagebox.showerror("错误", f"获取二维码失败:\n{str(e)}")

    def poll_login_status(self):
        """轮询检查登录状态"""
        while not self.login_status:
            try:
                ptqrtoken = self.calculate_ptqrtoken(self.qrsig)

                params = {
                    "u1": self.redirect_uri,
                    "ptqrtoken": ptqrtoken,
                    "ptredirect": "0",
                    "h": "1",
                    "t": "1",
                    "g": "1",
                    "from_ui": "1",
                    "ptlang": "2052",
                    "action": f"0-0-{int(time.time() * 1000)}",
                    "js_ver": "22052613",
                    "js_type": "1",
                    "login_sig": "",
                    "pt_uistyle": "40",
                    "aid": self.appid,
                    "daid": "383",
                }

                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                    "Referer": "https://xui.ptlogin2.qq.com/",
                    "Cookie": f"qrsig={self.qrsig}"
                }

                response = requests.get(
                    self.ptqrlogin_url,
                    params=params,
                    headers=headers,
                    allow_redirects=False  # 禁止自动重定向
                )
                response.encoding = "utf-8"
                content = response.text

                if "二维码未失效" in content:
                    continue
                elif "二维码认证中" in content:
                    self.root.after(0, lambda: self.status_var.set("扫码成功，请确认登录..."))
                elif "登录成功" in content:
                    # 保存Cookie和请求头信息
                    self.save_cookie_data(response)
                    self.root.after(0, self.handle_login_success, content)
                    break

                time.sleep(2)

            except Exception as e:
                print(f"轮询错误: {e}")
                time.sleep(5)

    def save_cookie_data(self, response):
        """保存Cookie和请求头信息到文件"""
        try:
            data_to_save = {
                "cookies": dict(response.cookies),
                "headers": dict(response.headers),
                "request_url": response.url,
                "status_code": response.status_code,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "qrsig": self.qrsig
            }

            # 确保目录存在
            self.cookie_file.parent.mkdir(parents=True, exist_ok=True)

            with open(self.cookie_file, "w", encoding="utf-8") as f:
                json.dump(data_to_save, f, ensure_ascii=False, indent=2)

            print(f"Cookie信息已保存到: {self.cookie_file}")

        except Exception as e:
            print(f"保存Cookie失败: {e}")
            self.root.after(0, lambda: messagebox.showerror("错误", f"保存Cookie失败: {e}"))

    def calculate_ptqrtoken(self, qrsig):
        """计算ptqrtoken"""
        e = 0
        for c in qrsig:
            e += (e << 5) + ord(c)
        return 2147483647 & e

    def handle_login_success(self, content):
        """处理登录成功"""
        self.login_status = True
        self.status_var.set("登录成功！Cookie已保存")

        messagebox.showinfo("成功",
                            f"登录成功！\nCookie信息已保存到:\n{self.cookie_file}")

        # 提取登录信息
        match = re.search(r"ptuiCB\('(.*?)'\)", content)
        if match:
            callback_str = match.group(1)
            parts = callback_str.split("','")
            if len(parts) >= 3:
                print(f"登录成功，跳转URL: {parts[2]}")


if __name__ == "__main__":
    root = tk.Tk()
    try:
        from ctypes import windll

        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass

    app = QQLoginApp(root)
    root.mainloop()