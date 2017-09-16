from django.test import TestCase
from todo.models import Task
from rest_framework import status
from api_v1.serializers import TaskSerializer

class TestUrlTodoIsAlive(TestCase):
    def test_index(self):
        resp = self.client.get('http://localhost:8000/todo-list/')
        self.assertEqual(resp.status_code,200)


