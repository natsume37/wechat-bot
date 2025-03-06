import logging
import logging.config
import os

# 路径配置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根目录
LOG_DIR = os.path.join(BASE_DIR, "log")  # 日志目录
INFO_LOG_PATH = os.path.join(LOG_DIR, "info.log")  # 信息日志路径
ERROR_LOG_PATH = os.path.join(LOG_DIR, "error.log")  # 错误日志路径

USER_DIR = os.path.join(BASE_DIR, 'db', 'users')  # 用户目录
FILE_DIR = os.path.join(BASE_DIR, 'db', 'files')  # 文件目录

# 确保日志目录存在
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LEVEL = 'INFO'

# 日志配置字典
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    # 日志格式
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(name)s] %(levelname)s [%(filename)s:%(lineno)d] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '%(asctime)s [%(name)s] %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    # 日志处理器
    'handlers': {
        'console': {
            'level': LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file_info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': INFO_LOG_PATH,
            'maxBytes': 10 * 1024 * 1024,  # 10MB
            'backupCount': 5,  # 保留5个备份文件
            'encoding': 'utf-8',
            'formatter': 'standard',
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': ERROR_LOG_PATH,
            'maxBytes': 10 * 1024 * 1024,  # 10MB
            'backupCount': 5,  # 保留5个备份文件
            'encoding': 'utf-8',
            'formatter': 'standard',
        },
    },
    # 日志记录器
    'loggers': {
        '': {  # 根日志记录器，捕获所有未明确配置的日志
            'handlers': ['console', 'file_info'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'error_logger': {  # 错误日志记录器
            'handlers': ['file_error'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}

# 应用日志配置
logging.config.dictConfig(LOGGING_CONFIG)

# 获取日志记录器
logger2 = logging.getLogger('server')  # 用于应用日志
error_logger = logging.getLogger('error_logger')  # 用于错误日志
asyncio_logger = logging.getLogger('asyncio')  # 用于asyncio错误日志
