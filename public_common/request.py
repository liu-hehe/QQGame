from functools import reduce
from typing import Callable
from bs4 import BeautifulSoup

import requests
import json
import datetime
from dateutil import tz
import logging
from public_common.log import logger
import re
from public_common.get_cookie import GetCookie
# logger = logging.getLogger(__name__)


class HTTPResponse:
    """响应对象包装"""

    def __init__(self, raw_rsp: requests.Response, request_threshold: int, fire_time: datetime.datetime = None,
                 session=None, **kwargs):
        """
        :param raw_rsp: requests原始的Response
        :param fire_time: 请求发送时间 local time date
        :param request_threshold: 慢请求阈值
        """
        self.session = session
        raw_rsp.encoding = 'utf-8'
        self.raw_rsp = raw_rsp
        self.func_mark = [kwargs.get('func_mark') if 'func_mark' in kwargs.keys() else None]
        self.rsp = self.parser(self.raw_rsp.text)
        self.deal_with_text = re.sub(r'\s+', ' ', BeautifulSoup(self.raw_rsp.text, 'xml').get_text(strip=True)).strip()
        self.request_threshold = request_threshold
        self.fire_time = fire_time or datetime.datetime.now(tz=tz.gettz('Asia/Shanghai'))
        self.log_myself()

    @staticmethod
    def parser(text: str):
        try:
            return json.loads(text)
        except Exception as e:
            if e:
                # logger.warning('无法解析JSON,返回原始数据')
                return text

    def __len__(self):
        return len(self.rsp)

    def __contains__(self, item):
        return item in self.rsp

    def __getitem__(self, item):
        if isinstance(item, str):
            if isinstance(self.rsp, str):
                logger.warning('返回结果无法解析为JSON对象')
                return None
            return self.rsp[item]

    def __getattr__(self, item):
        return self.raw_rsp.__getattribute__(item)

    def __str__(self):
        if self.raw_rsp.request.method == 'OPTIONS':
            return self.raw_rsp
        return self.raw_rsp.text

    @property
    def original_url(self):
        return self.raw_rsp.request.url

    @property
    def original_headers(self):
        return self.raw_rsp.request.headers

    @property
    def original_body(self):
        return self.raw_rsp.request.body

    @property
    def original_code(self):
        return self.raw_rsp.status_code

    @property
    def elapsed(self):
        return self.raw_rsp.elapsed.microseconds / 1000

    def log_myself(self):
        if self.elapsed >= self.request_threshold:
            logger.warning(f'请求响应时间[{self.elapsed}ms] >= [{self.request_threshold}ms]的慢请求警告阈值')

        logger.info(
            f"""
[model   ]:\t{self.func_mark[0] if self.func_mark else None}
[{self.raw_rsp.request.method}][{self.original_code}]:\t{self.original_url}
[datetime]:\t{self.fire_time}
[elapse  ]:\t{self.elapsed}ms
[headers ]:\t{self.original_headers}
[body    ]:\t{self.original_body}
[response]:\t{f"{self.deal_with_text}" if isinstance(self.deal_with_text, str) else self.raw_rsp.text}
"""
        )


class HTTPRequester:
    """HTTP接口请求包装类"""
    _before_url_concatenating: [Callable] = []
    _after_url_concatenating: [Callable] = []
    _before_send: [Callable] = []
    _after_send: [Callable] = []

    def __init__(self, func_mark=None, timeout=2000, request_threshold=3000):
        """
        :param host: host
        :param timeout: 超时时间(毫秒ms)
        :param request_threshold: 慢请求阈值(毫秒ms)
        """
        self.timeout_milliseconds = timeout
        self.timeout_seconds = timeout / 1000
        self.request_threshold = request_threshold
        self._session = None
        self.func_mark = func_mark
        # todo session retry

    @property
    def session(self):
        self._session = self._session or requests.session()
        return self._session

    def send(self, method: str, url: str, *args, **kwargs) -> HTTPResponse:

        # 读取config.ini文件中的cookie
        config_sections = GetCookie().get_cookie().sections()  # 获取config的key
        config_options_num = GetCookie.get_cookie().options(config_sections[0]) if config_sections else None  # 获取config的第一个key的所有value
        run_qq_num = GetCookie.get_cookie().get(config_sections[0], config_options_num[0]) if config_sections and config_options_num else None  # 获取config的第一个key的第一个value
        config_options = GetCookie.get_cookie().options(config_sections[1]) if config_sections else None  # 获取config的第二个key的所有value
        qq_cookie = GetCookie.get_cookie().get(config_sections[1], config_options[int(run_qq_num)-1]) if config_sections and config_options else None  # 获取第一个key的value当作变量控制运行qq号
        header = {'cookie': qq_cookie}

        now = datetime.datetime.now(tz=tz.gettz('Asia/Shanghai'))
        try:
            method, url, args, kwargs = reduce(lambda x, y: y(*x), self._before_send, (method, url, args, kwargs))
            rsp = self.session.request(method, url, timeout=self.timeout_seconds, headers=header, *args, **kwargs)
        except requests.exceptions.Timeout as e:
            raise e from None

        rsp = reduce(lambda x, y: y(x), self._after_send, rsp)

        wrapped_rsp = HTTPResponse(
            raw_rsp=rsp,
            fire_time=now,
            func_mark=self.func_mark,
            request_threshold=self.request_threshold,
            session=self.session,
            **kwargs
        )
        # 记录请求
        return wrapped_rsp

# params = {'zapp_uin': '', 'sid': '', 'channel': 0, 'g_ut': 1, 'cmd': 'worldtree', 'op': 'dostrengh', 'weapon_id': 1082}
# url = 'https://dld.qzapp.z.qq.com/qpet/cgi-bin/phonepk'
# print(HTTPRequester().send('get', url=url, params=params).rsp)