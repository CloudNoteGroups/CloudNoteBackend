from flask import Blueprint
from flask_restful import Api
from application.api.resources.note import NoteResource,NoteResource1
from application.api.resources.folder import FolderResources,FolderByIdResources
from application.api.resources.collect import CollectResource
bp = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(bp)

# 笔记表增删改查接口
api.add_resource(NoteResource,'/note')
api.add_resource(NoteResource1,'/note/<int:pk>')

# 文件夹表增删改查接口
api.add_resource(FolderResources,'/folder')
api.add_resource(FolderByIdResources,'/folder/<int:pk>')
api.add_resource(CollectResource,'/collect')