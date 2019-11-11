from flask_restful import fields
from flask import request
from flask_restful import Resource,marshal_with,reqparse
from application.api.model.models import Folder
from application.api.common.user import online
from application.api.common.response import response
from application.api.common.utils import time_format,get_db,model_to_dict

class FolderResources(Resource):

    def get_tree(self,base_page, dest_dict):
        dest_dict = {'folder_name': base_page.folder_name}
        children = base_page.parent
        if children:
            dest_dict['children'] = {}
            for child in children:
                self.get_tree(base_page, dest_dict)
        else:
            return


    def get(self):
        # 最傻的组织属性结构的方式
        first_folders = Folder.query.filter_by(user_id=online.user.user_id, parent_id=None).all()
        dest_dict = []
        for folder in first_folders:
            childrens = Folder.query.filter_by(user_id=online.user.user_id,parent_id=folder.folder_id).all()
            data = {
                'folder_id':folder.folder_id,
                'folder_name' :folder.folder_name,
                'add_time':folder.add_time,
                'children':[]
            }
            for child in childrens:
                data2 = {
                    'folder_id':child.folder_id,
                    'folder_name' :child.folder_name,
                    'add_time':child.add_time,
                    'children':[]
                }
                third_child = Folder.query.filter_by(user_id=online.user.user_id, parent_id=child.folder_id).all()
                for third in third_child:
                    thirdObj = Folder.query.filter_by(user_id=online.user.user_id, folder_id=third.folder_id).first()
                    print(third.folder_id)
                    if not thirdObj:
                        continue
                    data3 = {
                        'folder_id':thirdObj.folder_id,
                        'folder_name' :thirdObj.folder_name,
                        'add_time':thirdObj.add_time
                    }
                    data2['children'].append(data3)
                data['children'].append(data2)
            dest_dict.append(data)
        return response(dest_dict)

    def post(self):
        folder_name = request.form.get('folder_name')
        parent_id = request.form.get('parent_id')
        if not folder_name:
            return response('The folder name is null',message='params error',code=400)
        if len(folder_name) > 10:
            return response('The folder name is too long',message='params error',code=400)
        if parent_id:
            parentObj = Folder.query.filter_by(folder_id=parent_id).first()
            if parentObj.parent_id:
                parentObj = Folder.query.filter_by(folder_id=parentObj.parent_id).first()
                if parentObj.parent_id:
                    return response(message='Sorry,Can only support up to three levels of folders',code=201)

        folderObj = Folder(
            folder_name=folder_name,
            parent_id=parent_id,
            user_id=online.user.user_id,
            add_time=time_format()
        )
        db = get_db()
        db.session.add(folderObj)
        db.session.commit()

        return response({
            'folder_name':folder_name,
            'parent_id':parent_id
        })

class FolderByIdResources(Resource):
    def put(self,pk):
        folderObj = Folder.query.filter_by(folder_id=pk).first()
        if not folderObj:
            return response(message='source not found',code=404)
        folder_name = request.form.get('folder_name')
        print(folder_name)
        print(folderObj.folder_name)
        db = get_db()
        folderObj.folder_name = folder_name if folder_name else folderObj.folder_name
        db.session.commit()
        return response()
    def delete(self,pk):
        folderObj = Folder.query.filter_by(folder_id=pk).first()
        if not folderObj:
            return response(message='source not found', code=404)
        db = get_db()
        db.session.delete(folderObj)
        db.session.commit()
        return response()