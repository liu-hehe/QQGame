import os
import configparser

dir_path = os.path.dirname(os.path.dirname(__file__))
config_name = 'config.ini'
config_path = os.path.abspath(dir_path+'/config/'+config_name)


class GetCookie:
    """
    单例模式读取config.ini的cookie
    """
    _instance = None
    _cookie = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._load_cookie()  # 初始化加载cookie
        return cls._instance

    @classmethod
    def _load_cookie(cls):
        if not config_path and not os.path.isfile(config_path):
            raise ValueError(f'没有找到{config_name}文件')
        try:
            config = configparser.ConfigParser()
            config.read(config_path, encoding='utf-8')
            cls._cookie = config
        except Exception as e:
            raise RuntimeError(f'读取{config_name}失败')

    @classmethod
    def get_cookie(cls):
        return cls._cookie


if __name__ == '__main__':
    print(GetCookie().get_cookie().sections())