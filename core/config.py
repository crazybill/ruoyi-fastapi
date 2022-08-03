
class Config:

    APP_NAME = '若依FastAPI'
    APP_CODE = 'ruoyi'       # 应用编码，用于缓存key的前缀

    # 数据库
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'ruoyi'
    USERNAME = 'ruoyi'
    PASSWORD = 'admin'

    DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8'

    # redis 相关
    REDIS_URL = 'redis://localhost'
    REDIS_PORT = 6379
    REDIS_USER = 'root'
    REDIS_PASSWORD = 'admin'

    # token 相关配置
    ACCESS_TOKEN_EXPIRE_MINUTES = 60        # access token 过期时间，单位：分钟
    USER_TOKEN_EXPIRE_MINUTES = 60 * 24     # 客户端 Token 过期时间，默认为 1 天
    TOKEN_KEY = '5d0debda46d7a665acafb123456d05bf'      # 加密密钥，用 uuid.uuid4().hex 生成的32位字符串

