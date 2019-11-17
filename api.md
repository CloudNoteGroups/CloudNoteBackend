# CloudNote云笔记项目后端API文档
## 账号相关
### 登陆
1. 请求方式：http POST
2. 响应数据格式：json
3. 请求url: /api/account/login
4. 参数

|参数|类型|是否必须|描述|
|-|-|-|-|
|username|String|True|用户名|
|password|String|True|密码|

5. 响应数据
```
{
  "code":200,
  "data":{
    "token":"xxxxxxxx",
    "login":"true",
   },
   "message":"success"
}
```


### 注册
1. 请求方式：http POST
2. 响应数据格式：json
3. 请求url: /api/account/register
4. 参数

|参数|类型|是否必须|描述|
|-|-|-|-|
|username|String|True|用户名|
|password|String|True|密码|
|email|String|True|邮箱|
5. 响应数据
```
{
  "code":200,
  "data":{
    "error":"false",
    "msg":"注册成功",
    "username":username
   },
   "message":"success"
}
```

### 账号信息
1. 请求方式：http GET
2. 响应数据格式：json
3. 请求url: /api/account/user
4. 响应数据
```
{
  "code": 200, 
  "data": {
    "area": null, 
    "avatar": null, 
    "email": "1032298871@qq.com", 
    "gender": null, 
    "login_time": null, 
    "mobile": null, 
    "name": null, 
    "registered_time": "Sat, 09 Nov 2019 19:43:30 GMT", 
    "status": true, 
    "user_id": 8, 
    "username": "admin123"
  }, 
  "message": "success"
}

```




## 笔记(Note)
### 笔记列表
1. 请求方式：http GET
2. 响应数据格式：json
3. 请求url: /api/v1/note
4. 参数

|参数|类型|是否必须|描述|
|-|-|-|-|
|folder_id|Int|False|获取文件夹下的笔记|

5. 响应数据
```
{
    "code": 200,
    "message": "success",
    "data": [
        {
            "note_id": 7,
            "folder_id": 7,
            "title": "Go\u8bed\u8a00\u5e76\u53d1",
            "content": "# CloudNoteProject",
            "status": 1,
            "add_time": "Wed, 13 Nov 2019 23:01:46 -0000",
            "up_time": null
        },
        {
            "note_id": 16,
            "folder_id": 7,
            "title": "\u65b0\u7b14\u8bb0",
            "content": "",
            "status": 1,
            "add_time": "Thu, 14 Nov 2019 12:23:37 -0000",
            "up_time": null
        },
        {
            "note_id": 17,
            "folder_id": 7,
            "title": "\u65b0\u7b14\u8bb0",
            "content": "",
            "status": 1,
            "add_time": "Thu, 14 Nov 2019 12:23:59 -0000",
            "up_time": null
        }
    ]
}

```

### 添加笔记
1. 请求方式：http POST
2. 响应数据格式：json
3. 请求url：/api/v1/note
4. 参数

|参数|类型|是否必须|描述|
|-|-|-|-|
|title|String|True|标题|
|content|String|True|内容|
|folder_id|Int|False|将这个笔记保存在对应的文件夹下|

### 编辑笔记
1. 请求方式：http PUT
2. 响应数据格式：json
3. 请求url：/api/v1/note/<note_id>
4. 参数

|参数|类型|是否必须|描述|
|-|-|-|-|
|title|String|False|标题|
|content|String|False|内容|

### 删除笔记
1. 请求方式：http DELETE
2. 响应数据格式：json
3. 请求url：/api/v1/note/<note_id>

## 文件夹(Folder)
### 获取文件夹树
1. 请求方式：http GET
2. 响应数据格式：json
3. 请求url：/api/v1/folder
4. 响应数据
```
{
  "code": 200, 
  "data": [
    {
      "add_time": "Mon, 11 Nov 2019 21:22:39 GMT", 
      "folder_id": 6, 
      "folder_name": "Go"
      "children": [
        {
          "add_time": "Mon, 11 Nov 2019 21:23:12 GMT", 
          "folder_id": 7, 
          "folder_name": "GoWEB\u5f00\u53d1"
          "children": [
            {
              "add_time": "Mon, 11 Nov 2019 21:23:34 GMT", 
              "folder_id": 8, 
              "folder_name": "web\u6846\u67b6"
            }
          ], 
        }
      ]
    }
  ], 
  "message": "success"
}

```


### 添加文件夹
1. 请求方式：http POST
2. 响应数据格式：json
3. 请求url：/api/v1/folder
4. 参数

|参数|类型|是否必须|描述|
|-|-|-|-|
|folder_name|String|True|文件夹名|
|parent_id|Int|False|父级ID|

### 修改文件夹
1. 请求方式：http PUT
2. 响应数据格式：json
3. 请求url：/api/v1/folder/<folder_id>
4. 参数

|参数|类型|是否必须|描述|
|-|-|-|-|
|folder_name|String|True|文件夹名|

### 删除文件夹
1. 请求方式：http DELETE
2. 响应数据格式：json
3. 请求url：/api/v1/folder/<folder_id>

## 收藏笔记
### 收藏笔记列表
1. 请求方式：http GET
2. 响应数据格式：json
3. 请求url：/api/v1/collect

### 收藏笔记
1. 请求方式：http POST
2. 响应数据格式：json
3. 请求url：/api/v1/collect
4. 参数

|参数|类型|是否必须|描述|
|-|-|-|-|
|note_id|Int|True|笔记ID|


