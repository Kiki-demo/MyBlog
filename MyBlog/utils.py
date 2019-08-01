# coding:utf-8
import time
import os
import traceback
import sys

reload(sys)  # 总是报ascii 不能转unicode
sys.setdefaultencoding('utf-8')

import config

"""
自定义 Log 工具类
输出日志到cache文件中，收集日志
Config中的debug打开，控制台输出log信息，便于调试
"""


class Log(object):

    @staticmethod
    def i(tag, msg):
        """
        info级别的log信息
        :return: pass
        """
        log = "%s %s -info-： %s" % (time.strftime(config.LOG_TIME_FORMAT), tag, str(msg))
        if config.DEBUG:
            print(log)
        FileUtil.recordLog(log)

    @staticmethod
    def e(tag, msg):
        """
        error级别的log信息
        :return: pass
        """
        log = "%s %s -error-： %s" % (time.strftime(config.LOG_TIME_FORMAT), tag, msg)
        if config.DEBUG:
            print(log)
        FileUtil.recordLog(log)


"""
文件处理工具类
"""

FileUtil_TAG = "FileUtil"


class FileUtil(object):
    def __init__(self):
        pass

    @staticmethod
    def recordLog(log):
        """
        log写文件
        :param log: 要写入的log内容
        :return: 写入状态
        """
        result = False
        filePath = config.LOG_DIR + config.LOG_FILE
        try:
            if not os.path.exists(config.LOG_DIR):
                os.mkdir(config.LOG_DIR)
            with open(filePath, 'a+') as f:
                f.write(log + "\n")
            result = True
        except Exception, reason:
            Log.e(FileUtil_TAG, "record log fail!\n reason:%s \n traceback:%s \n log: %s" % (
                repr(reason), traceback.format_exc(), log))
        return result


def convert_to_dict(obj):
    """
    把Object Bean 对象转换成Dict字典
    :param obj:object对象
    :return:{}字典
    """
    dict = {}
    dict.update(obj.__dict__)
    return dict
