import os


# 定义密钥
SECRET_KEY = "HuXianSen_JYWuLiu"

# 数据库设置
SQLALCHEMY_DATABASE_URI = "mysql://" + os.getenv("DATABASE_USER") + ":" + os.getenv("DATABASE_PASSWORD") \
                          + "127.0.0.1:3306/wuliu"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 邮箱设置
# 发送者邮箱的服务器地址
MAIL_SERVER = "smtp.qq.com"

# MAIL_USE_TLS:端口号587
# MAIL_USE_SSL:端口号465
# QQ邮箱不支持非加密方式发送邮件
MAIL_PORT = 587
MAIL_USE_TLS = True
# MAIL_USE_SSL = False
MAIL_USERNAME = "599663430@qq.com"
# 邮箱的授权码
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
MAIL_DEFAULT_SENDER = "599663430@qq.com"

# Redis缓存设置
CACHE_TYPE = 'redis'
CACHE_REDIS_HOST = '127.0.0.1'
CACHE_REDIS_PORT = 6379
CACHE_REDIS_DB = ''
CACHE_REDIS_PASSWORD = ''
