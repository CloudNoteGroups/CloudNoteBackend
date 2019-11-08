# 已实现接口
## 登陆
request
```
url:/api/account/login
method:POST
formdata:
    username:xxx
    password:xxx
```

response
```
success
{
    'code':1,
    'token':'xxxxxxx'
}

error
{
    'code':0,
    'msg':'登陆失败，账号或者密码错误'
}
```

## 注册
request
```
url:/api/account/login
method:POST
formdata:
    username:xxx
    password:xxx
    email:xxx
```
response
```
success
{
    "code":"1",
    "msg":"注册成功",
    "username":"username"
}

error
{
    "code":"0",
    ...对应的错误提示
}

```