import pytest
import json

import app


class Test_TodoApp:

    def setUp(self):
        self.app = app.test_client()

    def test_get_api(self, client):
        response = client.get('/api/v1/tasks')
        
        assert response.status_code == 200

    def test_get_api_resposne(self, client):
        response = client.get('/api/v1/tasks')
        res_payload = response.json
        tasks = res_payload['tasks']
        assert isinstance(tasks, list)

    def test_delete_api(self, client):
        response = client.delete('/api/v1/task/5')
        status = response.status_code
        
        assert status == 200

        ## After deleting record checking records length
        ## It should be 4 now
        response = client.get('/api/v1/tasks')
        res_payload = response.json
        tasks = len(res_payload['tasks'])
        assert tasks == 4
