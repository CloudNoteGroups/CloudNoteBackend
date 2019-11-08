from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for,jsonify
)
from application.api.common.utils import config,md5,get_db,time_format,model_to_dict
bp = Blueprint('user', __name__, url_prefix='/api/account')
from application.api.model.models import UserInfo,Token
import time
import re
@bp.route('/login',methods=['POST'])
def login():
    """
    登陆接口,登陆成功后返回token
    :return: json
    """
    username = request.form.get('username',None)
    password = request.form.get('password',None)
    userObj = UserInfo.query.filter_by(username=username,password=md5(password)).first()

    if userObj:
        ## 先将之前的删除
        db = get_db()
        remove_token = Token.query.filter_by(user_id=userObj.user_id).first()
        if remove_token:
            db.session.delete(remove_token)
            db.session.commit()
        # 登陆成功
        token = md5(md5(username)+md5(userObj.email)+md5(str(time.time())))
        tokenObj = Token(
            user_id=userObj.user_id,
            token=token,
            expire_date=time_format(offset=config('TOKEN_VALIDITY'))
        )
        db.session.add(tokenObj)
        db.session.commit()
        return jsonify({
            'code':1,
            'token':token
        })

    return jsonify({
        'code':0,
        'msg':'登陆失败，账号或者密码错误'
    })

@bp.route('/register',methods=['POST'])
def register():
    """
    注册接口
    :return:
    """
    username = request.form.get('username',None)
    password = request.form.get('password',None)
    email = request.form.get('email',None)
    error = {}
    if username:
        if len(username) > 16 or len(username) < 6:
            error['username'] = '用户名长度：6-16位'
        if re.match(r'^[0-9]+$',username) or re.match(r'^_|_$',username):
            error['username'] = '请正确填写用户名'

        userObj = UserInfo.query.filter_by(username=username).first()
        if userObj:
            error['username'] = '用户名重复了'
    else:
        error['username'] = '请填写用户名'

    if password:
        if len(password) < 6:
            error['password'] = '用户名最短为6位'

        if re.match(r'^[0-9]+$',password):
            error['password'] = '密码不能全部是数字'

    else:
        error['password'] = '请输入密码'

    if email:
        if len(email) > 7:
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) == None:
                error['email'] = '请输入正确的邮箱格式'
        else:
            error['email'] = '请输入正确的邮箱格式'

        userObj = UserInfo.query.filter_by(email=email).first()
        if userObj:
            error['email'] = '邮箱重复了'
    else:
        error['email'] = '请填写邮箱'

    if not error:
        userInfo = UserInfo(
            username=username,
            password=md5(password),
            email=email,
            registered_time=time_format()
        )
        db = get_db()
        db.session.add(userInfo)
        db.session.commit()
        response = {
            'Code':1,
            'msg':'注册成功',
            'username':username,
        }
        return jsonify(response)
    return jsonify(error)

