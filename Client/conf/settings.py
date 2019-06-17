import os

# 数据要发送到的服务器地址
Params = {
    "server": "127.0.0.1",
    'port': 8000,
    'url': '/assets/report/',
    'request_timeout': 30,
}

# 配置日志
PATH = os.path.join(os.path.dirname(os.getcwd()), 'log', 'cmdb.log')
