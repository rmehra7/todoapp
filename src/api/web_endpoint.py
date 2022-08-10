from flask import request, send_file, render_template
from flask_restplus import Api, Resource, fields

from services.todo_service import TodoService
from common import constant
from api.rest_endpoint import app, task_object
from server.app_server import server

app = server.app

@app.route('/tasks', methods=['GET'])
def index():
    tasks = task_object.get_all_tasks()
    return render_template('index.html', tasks=tasks)
