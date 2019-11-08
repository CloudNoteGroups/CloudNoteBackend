# 后端目录说明
```
backend
│  config.py // flask配置文件
│  README.md 
│  setup.py  // 入口程序
├─application
│  │  __init__.py
│  │
│  └─api
│     ├─common // 公共函数
│     │  └─utils.py 
│     │  
│     ├─controller //控制器
│     │  └─account.py
│     │
│     ├─logic // 逻辑
│     └─model // 模型
│
└─instance

```
# 环境搭建
## 数据库
数据库配置在根目录的config.py中配置类中的SQLALCHEMY_DATABASE_URI属性，比如配置debug模式（DebugMode）的SQLALCHEMY_DATABASE_URI
```
class DebugMode(CommonConfig):
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/cloud_note'
  
```
将数据库的用户名、密码、端口、数据库名(先在你的数据库中新建这个数据库)换成你的就可以了

## Python环境
在我本地的Python环境是3.7.2

安装依赖库：
```
pip install -r requirements.txt
```

## 生成数据表并运行
```
python run.py install
```

# 访问
```
127.0.0.1:5000/hello
```