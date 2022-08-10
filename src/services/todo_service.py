import copy

from database.todoapp_models import TODO_LIST


class TodoService:

    todo_list = copy.deepcopy(TODO_LIST)

    def get_last_id(self):
        last_task = self.todo_list[-1]
        return last_task['id'] + 1

    def get_task(self, taskid):
        """Get specific task by id."""
        task = [task for task in self.todo_list if task['id'] == taskid]
        if task:
            return task
        return False

    def get_all_tasks(self):
        """Get all tasks"""
        return self.todo_list

    def delete_task(self, taskid):
        """Delete task by id"""
        tasks_count = len(self.todo_list)
        self.todo_list = [task for task in self.todo_list if task['id'] != taskid]
        after_delete_tasks_count = len(self.todo_list)
        if tasks_count != after_delete_tasks_count:
            return True
        return False

    def add_task(self, payload):
        """Add new record"""
        payload['id'] = self.get_last_id()
        self.todo_list.append(payload)
        return True

    def update_task(self, taskid, payload):
        """Update existing record"""
        ## check record exist
        task = [task for task in self.todo_list if task['id'] == int(taskid)]
        if not task:
            return False
        index = self.todo_list.index(task[0])
        for key, value in payload.items():
            if key in ['task', 'datetime', 'is_completed'] and value:
                self.todo_list[index][key] = value
        return True
