from application import create_app
from application.api.model.models import db
import hashlib
import time
def config(name=None):
    conf = create_app().config
    if name:
        return conf.get(name,None)
    return conf


def md5(string:str):
    hl = hashlib.md5()
    hl.update(string.encode("utf-8"))
    return hl.hexdigest()

def get_db():
    return db

def get_db_session():
    return db.session

def time_format(format="%Y-%m-%d %H:%M:%S",offset=0):
    timetmp = time.time() + offset
    localTime = time.localtime(timetmp)
    strTime = time.strftime(format, localTime)
    return strTime



def model_to_dict(result):
    from collections import Iterable
    # 转换完成后，删除  '_sa_instance_state' 特殊属性
    try:
        if isinstance(result, Iterable):
            tmp = [dict(zip(res.__dict__.keys(), res.__dict__.values())) for res in result]
            for t in tmp:
                t.pop('_sa_instance_state')
        else:
            tmp = dict(zip(result.__dict__.keys(), result.__dict__.values()))
            tmp.pop('_sa_instance_state')
        return tmp
    except BaseException as e:
        print(e.args)
        raise TypeError('Type error of parameter')

