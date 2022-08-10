from flask import request, send_file
from flask_restplus import Api, Resource, fields

from server.app_server import server
from services.todo_service import TodoService
from common import constant

app, api = server.app, server.api
todoapis = api.namespace('Tasks', description="Todo task.", path='/')
task_object = TodoService()

task_fields = api.model('Tasks', {
    'task': fields.String,
    'datetime': fields.DateTime
})

@todoapis.route('/api/v1/tasks')
class Tasks(Resource):

    def get(self):
        """To fetch one or all tasks."""
        response = {
            "msg": constant.FETCH_MESSAGE,
            "status_code": 200
        }

        response["tasks"] = task_object.get_all_tasks()
        return response

    @todoapis.expect(task_fields)
    def post(self):
        """Create task"""
        request_data = request.json
        add_task = task_object.add_task(request_data)
        if add_task:
            return {
                "msg": constant.CREATE_MESSAGE,
                "status_code": 200,
                "tasks": []
            }

        return {
            "msg": constant.INVALID_INPUT,
            "status_code": 409,
            "tasks": []
        }

    
@todoapis.route('/api/v1/task/<int:taskid>')
class Task(Resource):

    def get(self, taskid=None):
        """To fetch one or all tasks."""
        if not taskid:
            return {
                "msg": constant.NOT_FOUND,
                "status_code": 404,
                "tasks": []
            }

        response = {
            "msg": constant.FETCH_MESSAGE,
            "status_code": 200,
            "tasks": task_object.get_task(taskid)
        }

        return response

    @todoapis.expect(task_fields)
    def put(self, taskid):
        """Update task"""
        if not taskid:
            return {
                "msg": constant.NOT_FOUND,
                "status_code": 404,
                "tasks": []
            }
        request_data = request.json
        task_object.update_task(taskid, request_data)
        return {
            "msg": constant.UPDATE_MESSAGE,
            "status_code": 406,
            "tasks": []
        }

    def delete(self, taskid):
        """Delete task"""
        if not taskid:
            return {
                "msg": constant.NOT_FOUND,
                "status_code": 404,
                "tasks": []
            }

        delete_rec = task_object.delete_task(taskid)
        if delete_rec:
            return {
                "msg": constant.DELETE_MESSAGE,
                "status_code": 200,
                "tasks": []
            }
        return {
            "msg": constant.INVALID_TASK_ID,
            "status_code": 406,
            "tasks": []
        }
