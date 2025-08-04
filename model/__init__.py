from functools import wraps
from copy import deepcopy
from public_common.request import HTTPRequester
import requests
import re
import time
url = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk'
params = {'zapp_uin': '', 'sid': '', 'channel': 0, 'g_ut': 1, 'cmd': ''}
error_message = ['很抱歉，系统繁忙，请稍后再试', '矿石商店操作频繁']


class RequestSend:
    """
    发送请求带参数类装饰器
    """
    def __init__(self, re_exp=None, max_retries=5, retry_interval=1, **kwargs):
        self.params = deepcopy(params)
        self.re_exp = deepcopy(re_exp)
        self.max_retries = max_retries  # 最大重试次数
        self.retry_interval = retry_interval  # 重试间隔(秒)
        if kwargs:
            for k, v in kwargs.items():
                self.params[k] = v

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self.re_exp = kwargs.pop('re_exp', self.re_exp)  # 原函数调用时传入的re_exp会覆盖装饰器转入的参数re_exp，并删除kwargs的re_exp
            merged_params = deepcopy(self.params)
            merged_params.update(kwargs)  # 原函数调用时传入的kwargs会覆盖装饰器参数kwargs
            merged_params.update(args[0]) if args and isinstance(args[0], dict) else None  # 原函数传入位置参数，且位置参数为字典类型
            args = ()  # 清空args，防止传入HTTPRequester引起报错
            kwargs.clear()  # 清空kwargs，防止传入HTTPRequester引起报错
            func_mark = func.__doc__
            retry_count = 0  # 重试次数
            while retry_count < self.max_retries:  # 重试次数小于最大重试次数时，重新发送请求
                try:
                    func(*args, **kwargs)
                    response = HTTPRequester(func_mark=func_mark).send('get', url=url, params=merged_params, *args, **kwargs)
                    response_deal_with = response.deal_with_text
                    if all(error not in response_deal_with for error in error_message):  # 判断error中的每个元素都不在response_deal_with中存在
                        if self.re_exp:
                            match_str = re.findall(f"{self.re_exp}", response.raw_rsp.text)
                            return match_str
                        else:
                            return response
                    retry_count += 1  # 重试一次retry_count的值+1
                    if retry_count < self.max_retries:  # 重试次数小于最大重试次数时，等待1秒
                        time.sleep(self.retry_interval)
                # 捕获ReadTimeout异常，继续重试
                except requests.exceptions.ReadTimeout:
                    pass
                # 其他异常直接抛出
                except Exception as e:
                    raise e
            # 达到最大重试次数后仍然失败
            raise Exception(f"请求失败，达到最大重试次数 {self.max_retries} 次后仍然收到错误消息: {error_message}")
        return wrapper
