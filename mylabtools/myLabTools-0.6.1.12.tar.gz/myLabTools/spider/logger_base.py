import logging
from logging import handlers
import time

class Logger(object):
    """日志 工具类

    """    
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }  # 日志级别关系映射
    T = time.strftime("%m/%d %H:%M:%S")  # 程序开始运行的时间
    def __init__(self,filename, level='info', when='D', backCount=3,
                 fmt="%(asctime)s - %(levelname)s  - %(message)s"):
        """日志工具

        Args:
            filename (_type_): 日志保存的路径
            level (str, optional): 日志的级别. Defaults to 'info'.
            when (str, optional): 时间. Defaults to 'D'.
            backCount (int, optional): _description_. Defaults to 3.
            fmt (str, optional): 日志的格式. Defaults to "%(asctime)s - %(levelname)s  - %(message)s".
        """        
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别
        sh = logging.StreamHandler()  # 往屏幕上输出
        sh.setFormatter(format_str)  # 设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,
                                               encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)  # 设置文件里写入的格式
        self.logger.addHandler(sh)  # 把对象加到logger里
        self.logger.addHandler(th)


if __name__ == '__main__':
    log = Logger('all.log', level='debug')
    logger = log.logger
    logger.debug('debug')
    logger.info('info')
    logger.warning('警告')
    logger.error('报错')
    logger.critical('严重')