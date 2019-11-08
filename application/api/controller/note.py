from flask_restful import Api,Resource,fields,marshal_with
from flask import (
    Blueprint
)
note_bp = Blueprint('note', __name__, url_prefix='/api/note')
api = Api(note_bp)

class NoteClass():
    def __init__(self,title,content):
        self.title = title
        self.content = content

class NoteControll(Resource):
    resource_fields = {
        'title':fields.String(default='标题',attribute="title"),
        'content':fields.String(default="")
    }
    @marshal_with(resource_fields)
    def get(self):
        res = NoteClass('标题','内容')
        return res

api.add_resource(NoteControll,'/',endpoint='note')