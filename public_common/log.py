import sys
import os
import logging
import datetime
time_day = datetime.datetime.now().strftime('%Y-%m-%d')
log_name = f'{time_day}.log'
log_path = r'D:\qq_game\data'
log_file_path = os.path.join(log_path, log_name)
print(os.path.join(os.path.dirname(log_path), 'config'))

# 1. 创建Logger实例
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # 设置最低日志级别

# 2. 创建控制台处理器（打印到屏幕）
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # 控制台只输出INFO及以上级别

# 3. 创建文件处理器（保存到文件）
file_handler = logging.FileHandler(log_file_path, encoding='utf-8')
file_handler.setLevel(logging.DEBUG)  # 文件记录所有DEBUG及以上级别

console_handler.stream = sys.__stdout__  # 使用原生标准输出，避免颜色注入

# 4. 设置日志格式
formatter = logging.Formatter()
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 5. 将处理器添加到Logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
