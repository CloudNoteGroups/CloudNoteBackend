from flask_restful import fields
from flask_restful import Resource,marshal_with,reqparse
from flask import request
from application.api.common.user import online
from application.api.model.models import Note
from application.api.common.utils import time_format,get_db,model_to_dict

note_fields = fields.Nested({
    'note_id': fields.Integer(),
    'folder_id': fields.Integer(default=0),
    'title': fields.String(attribute='title'),
    'content': fields.String(attribute='content'),
    'status': fields.Integer(default=1),
    'add_time': fields.DateTime(),
    'up_time': fields.DateTime(),
    'is_collect':fields.Boolean()

})
class NoteResource(Resource):
    base_fields = {
        'code':fields.Integer(default=200),
        'message':fields.String(default='success')
    }
    resource_fields = base_fields
    resource_fields['data'] = fields.List(note_fields)
    @marshal_with(resource_fields)
    def get(self):
        where = {
            'user_id':online.user.user_id
        }
        folder_id = request.args.get('folder_id',None)
        if folder_id:
            where['folder_id'] = folder_id
        noteList = Note.query.filter_by(**where).all()
        # 判断自己的笔记列表是否有已收藏的
        for note in noteList:
            if note.collect:
                for collect in note.collect:
                    if collect.user_id == online.user.user_id:
                        note.is_collect = True
                        break
                else:
                    note.is_collect = False
            else:
                note.is_collect = False
        res = {
            'code':200,
            'message':'success',
            'data':noteList
        }
        return res

    def post(self):
        form = request.get_json()
        if request.headers['Content-Type'] == 'application/json;charset=UTF-8':
            title = form.get('title','')
            content = form.get('content','')
            folder_id = form.get('folder_id',None)
        else:
            title = request.form.get('title','')
            content = request.form.get('content','')
            folder_id = request.form.get('folder_id',None)
        noteObj = Note(
            user_id = online.user.user_id,
            title=title,
            content=content,
            folder_id=folder_id,
            status=1,
            add_time=time_format()
        )
        db = get_db()
        db.session.add(noteObj)
        db.session.commit()
        print(noteObj.note_id)
        data = {
            'note_id':noteObj.note_id,
            'title':title,
            'content':content
        }
        res = {
            'code':200,
            'message':'success',
            'data':data

        }
        return res



class NoteResource1(Resource):
    resource_fields = {
        'code':fields.Integer(default=200),
        'message':fields.String(default='success'),
        'data':note_fields
    }
    def put(self,pk):
        noteObj, flag = self.verify(pk)
        if not flag:
            return noteObj
        form = request.get_json()
        if request.headers['Content-Type'] == 'application/json;charset=UTF-8':
            title = form.get('title', '')
            content = form.get('content', ''),
        else:
            title = request.form.get('title')
            content = request.form.get('content')

        noteObj.title = title
        noteObj.content = content if content else noteObj.content
        noteObj.up_time = time_format()
        db = get_db()
        db.session.commit()

        return {
            'code':200,
            'message':'success'
        }

    def delete(self,pk):
        noteObj,flag = self.verify(pk)
        if not flag:
            return noteObj
        db = get_db()
        [db.session.delete(note) for note in noteObj.collect] # 批量将外键删除
        db.session.delete(noteObj)
        db.session.commit()
        return {
            'code':200,
            'message':'success'
        }

    def verify(self,pk):
        noteId = pk
        if not noteId:
            return {
                'code': 201,
                'message': 'note_id Params Is Null'
            },False
        noteObj = Note.query.filter_by(note_id=noteId).first()
        if not noteObj:
            return {
                'code': 201,
                'message': 'Data Does Not Exist'
            },False
        if noteObj.user_id != online.user.user_id:
            return {
                'code': 201,
                'message': 'Only Delete Your Own Notes'
            },False
        return noteObj,True

    @marshal_with(resource_fields)
    def get(self,pk):
        noteObj = Note.query.filter_by(note_id=pk).first()
        if not noteObj:
            return {
                'code':404,
                'message':'Data Does Not Exist'
            }
        return {
            'data':noteObj
        }
