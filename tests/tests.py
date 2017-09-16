from django.test import TestCase
from todo.models import Task
from rest_framework import status
from api_v1.serializers import TaskSerializer

class TestUrlTodoIsAlive(TestCase):
    def test_index(self):
        resp = self.client.get('http://localhost:8000/todo-list/')
        self.assertEqual(resp.status_code,200)


class TestGetTasksSucess(TestCase):
    def setUp(self):
        for i in range(1,3):
            Task.objects.create(description='tasks {}'.format(i))

    def test_index(self):
        
        response = self.client.get('http://localhost:8000/todo-list/api/v1/tasks/')
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)