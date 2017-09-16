from django.test import TestCase
from todo.models import Task
from rest_framework import status
from api_v1.serializers import TaskSerializer
import json
class TestUrlTodoIsAlive(TestCase):
    def test_index(self):
        resp = self.client.get('http://localhost:8000/todo-list/')
        self.assertEqual(resp.status_code,200)


class TestGetTasksSucess(TestCase):
    def setUp(self):
        for i in range(1,3):
            Task.objects.create(description='tasks {}'.format(i), index=i)

    def test_index(self):
        
        response = self.client.get('http://localhost:8000/todo-list/api/v1/tasks/')
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

class TestCreateTasksSucess(TestCase):
    
    def test_index(self):
        data = {'description': 'tasks','index':1}
        response = self.client.post('http://localhost:8000/todo-list/api/v1/tasks/', data=data)
        tasks = Task.objects.get(description='tasks')
        serializer = TaskSerializer(tasks)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializer.data)

class TestRenameTasksSucess(TestCase):
    def setUp(self):
        self.create_task = Task.objects.create(description='tasks created', index=1)
        
    def test_index(self):
        data = {"description": "tasks rename"}
        url = 'http://localhost:8000/todo-list/api/v1/tasks/{}/'.format(self.create_task.id)
        
        response = self.client.put( url, data=json.dumps(data), content_type='application/json')
        
        serializer = TaskSerializer(self.create_task)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('description'), data['description'])

class TestMarkDoneTasksSucess(TestCase):
    def setUp(self):
        self.create_task = Task.objects.create(description='tasks created', index=1)
        
    def test_index(self):
        data = {"done": True}
        url = 'http://localhost:8000/todo-list/api/v1/tasks/{}/'.format(self.create_task.id)
        
        response = self.client.put( url, data=json.dumps(data), content_type='application/json')
        serializer = TaskSerializer(self.create_task)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('done'), True)

class TestMarkDeletedTasksSucess(TestCase):
    def setUp(self):
        self.create_task = Task.objects.create(description='tasks created', index=1)
        
    def test_index(self):
        
        url = 'http://localhost:8000/todo-list/api/v1/tasks/{}/'.format(self.create_task.id)
        
        response = self.client.delete( url, content_type='application/json')
        serializer = TaskSerializer(self.create_task)
        task = Task.objects.filter(pk=self.create_task.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        assert task.count() == 0