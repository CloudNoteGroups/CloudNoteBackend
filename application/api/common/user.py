from flask import request
from application.api.model.models import UserInfo,Token
class Online():
    _instance = None
    user = None
    def __init__(self):
        pass
    @classmethod
    def instance(cls):
        if not cls._instance:

            obj = cls()
            cls._instance = obj
        return cls._instance

online = Online.instance()