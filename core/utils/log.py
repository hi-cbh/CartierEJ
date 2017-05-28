# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""小红书日志模块"""

import os
import yaml
import logging.config

from core.utils.constant import PROJECT_PATH, RESOURCE_PATH

_LOG_FILE_DIRECTORY = os.path.abspath(os.path.join(PROJECT_PATH, "logs"))

# 如果文件不存在，创建文件目录
if not os.path.exists(_LOG_FILE_DIRECTORY):
    os.mkdir(_LOG_FILE_DIRECTORY)

_LOGGER_CONFIG_PATH = os.path.join(RESOURCE_PATH, "logger_config.yml")

with open(_LOGGER_CONFIG_PATH, 'r') as f:
    log_config = yaml.load(f)
logging.config.dictConfig(log_config['logging'])

# 全局变量
LOGGER = logging.getLogger('')

if __name__ == '__main__':
    LOGGER.info("Root logger")
