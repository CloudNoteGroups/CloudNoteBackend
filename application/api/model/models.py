from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class UserInfo(db.Model):
    """
    UserInfo表模型
    """
    __tablename__ = 'userinfo'

    user_id =db.Column(db.Integer,primary_key=True,autoincrement=True,comment="用户ID")
    username = db.Column(db.String(64),unique=True,nullable=False,comment="用户名")
    password = db.Column(db.String(128),nullable=False,comment="密码")
    name = db.Column(db.String(32),comment="昵称")
    avatar = db.Column(db.String(64),comment="头像")
    gender = db.Column(db.Integer,comment="性别")
    email = db.Column(db.String(32),nullable=False,comment="邮箱")
    status = db.Column(db.Boolean,default=True,comment="账号状态")
    mobile = db.Column(db.Integer,comment="手机号码")
    registered_time = db.Column(db.DateTime,comment="注册时间")
    login_time = db.Column(db.DateTime,comment="最近登陆时间")
    area = db.Column(db.String(128),comment="地区")



class Folder(db.Model):
    __tablename__ = 'folder'
    folder_id = db.Column(db.Integer,primary_key=True,autoincrement=True,comment="文件夹ID")
    user_id = db.Column(db.Integer,db.ForeignKey('userinfo.user_id'),nullable=False,comment="用户ID")
    user = db.relationship('UserInfo',backref=db.backref('folders', lazy=True))

    folder_name = db.Column(db.String(16),nullable=False,comment="文件夹名")

    parent_id = db.Column(db.Integer,db.ForeignKey('folder.folder_id'),nullable=True,comment="自关联") # 自关联
    parent =  db.relationship("Folder", remote_side=[folder_id], backref='folder')
    # children = db.relationship("Folder", backref=db.backref("parent", remote_side=folder_id))

    add_time = db.Column(db.DateTime,comment="加入时间")

class Note(db.Model):
    __tablename__ = 'note'
    note_id = db.Column(db.Integer,primary_key=True,autoincrement=True,comment="笔记ID")
    folder_id = db.Column(db.Integer,db.ForeignKey('folder.folder_id'),nullable=True,comment="文件夹ID")

    user_id = db.Column(db.Integer, db.ForeignKey('userinfo.user_id'), nullable=False, comment="用户ID")
    user = db.relationship('UserInfo', backref=db.backref('note', lazy=True))

    folder = db.relationship("Folder", backref=db.backref('note', lazy=True))
    title = db.Column(db.String(64),comment="笔记标题")
    content = db.Column(db.Text,comment="笔记内容")
    status = db.Column(db.Integer,default=1,nullable=False,comment="笔记状态")
    password = db.Column(db.String(128),comment="加密文档密码")
    add_time = db.Column(db.DateTime)
    up_time = db.Column(db.DateTime)

class Collect(db.Model):
    __tablename__ = 'collect'
    collect_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('userinfo.user_id'), nullable=False,comment="用户ID")
    user = db.relationship('UserInfo', backref=db.backref('collect', lazy=True))
    note_id = db.Column(db.Integer, db.ForeignKey('note.note_id'), nullable=False,comment="笔记ID")
    note = db.relationship('Note', backref=db.backref('collect', lazy=True))
    add_time = db.Column(db.DateTime)
    myself = db.Column(db.Boolean,comment="是否是自己的笔记")


class Shared(db.Model):
    __tablename__ = 'shared'
    shared_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('userinfo.user_id'), nullable=False,comment="用户ID")
    user = db.relationship('UserInfo', backref=db.backref('shared', lazy=True))
    note_id = db.Column(db.Integer, db.ForeignKey('note.note_id'), nullable=False,comment="笔记ID")
    note = db.relationship('Note', backref=db.backref('shared', lazy=True))


class Token(db.Model):
    __tablename__ = 'token'
    token_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    token = db.Column(db.String(128),comment='校验字段')
    user_id = db.Column(db.Integer, db.ForeignKey('userinfo.user_id'), nullable=False, comment="用户ID")
    user = db.relationship('UserInfo', backref=db.backref('token', lazy=True))
    expire_date = db.Column(db.DateTime,comment="token过期时间")
