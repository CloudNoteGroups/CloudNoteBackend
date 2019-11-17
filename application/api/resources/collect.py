from flask_restful import fields
from flask_restful import Resource,marshal_with,reqparse
from flask import request
from application.api.common.user import online
from application.api.model.models import Collect,Note
from application.api.common.response import response
from application.api.common.utils import time_format,get_db,model_to_dict
base_fields = {
        'code': fields.Integer(default=200),
        'message': fields.String(default='success')
    }
collect_fields = fields.Nested({
    'note_id': fields.Integer(),
    'title': fields.String(attribute='title'),
    'content': fields.String(attribute='content'),
    'status': fields.Integer(default=1),
    'add_time': fields.DateTime(),
    'up_time': fields.DateTime(),
})
resource_fields = base_fields
resource_fields['data'] = fields.List(collect_fields)
class CollectResource(Resource):

    @marshal_with(resource_fields)
    def get(self):
        print(online.user.collect[0].note)
        collects = online.user.collect
        note_list = []
        for collect in collects:
            note_list.append(
                collect.note
            )
        return {
            'message':'success',
            'code':200,
            'data':note_list
        }

    def post(self):
        form = request.get_json()
        if not form:
            return response(message='请传入必须的数据',code=201)
        note_id = form.get('note_id')
        noteObj = Note.query.filter_by(note_id=note_id).first()
        if  not noteObj:
            return response(message='没有找到这个笔记',code=201)
        isself = True if noteObj.user_id==online.user.user_id else False

        collect = Collect(
            user=online.user,
            note=noteObj,
            myself=isself,
            add_time=time_format()
        )
        db = get_db()
        db.session.add(collect)
        db.session.commit()
        return response(message='success',code=200)

    def delete(self):
        form = request.get_json()
        if not form:
            return response(message='请传入必须的数据', code=201)
        note_id = form.get('note_id')
        noteObj = Note.query.filter_by(note_id=note_id).first()

        if not noteObj:
            return response(message='没有找到这个笔记', code=201)
        collectObj = Collect.query.filter_by(
            user_id=online.user.user_id,
            note_id=note_id
        ).first()
        db = get_db()
        db.session.delete(collectObj)
        db.session.commit()
        return response()