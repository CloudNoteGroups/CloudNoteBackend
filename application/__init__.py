import os
from flask import Flask,request
from application.api.model.models import Token,UserInfo
from application.api.common.response import response
from application.api.common.user import online

import time
def create_app(test_config=None):
    # global db
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        from config import TestingMode,DebugMode,ProductionMode
        app.config.from_object(DebugMode)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # db.init_app(app)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello World'

    # 引入对应的app注册
    from application.api.controller import account
    from application.api import api
    app.register_blueprint(api.bp)
    app.register_blueprint(account.bp)
    return app
app = create_app()


def str_to_timestamp(str=None,format='%Y-%m-%d %H:%M:%S'):
    # 格式化好的时间转时间戳的,如果不传格式化好的时间，就返回当前的时间戳
    if str:
        return int(time.mktime(time.strptime(str,format)))
    else:
        return int(time.time())

@app.before_request
def before_request():
    """
    token校验
    :return:
    """
    path = request.path
    if path not in app.config['EXCLUDE_URL']:
        token = request.headers.get('token', None)
        if not token:
            return response(message="not auth",code="401")

        tokenObj = Token.query.filter_by(token=token).first()
        if not tokenObj:
            return response(message="not auth",code="401")
        userObj = UserInfo.query.filter_by(user_id=tokenObj.user_id).first()
        if not userObj:
            return response(message="not auth",code="401")
        online.user = userObj
        now_time = time.time()
        expire_date = str_to_timestamp(str(tokenObj.expire_date))
        if expire_date <= now_time:
            return response(message="not auth",code="401")
