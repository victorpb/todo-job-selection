from django.shortcuts import render
from django.views.generic import View


class TodoView(View):
    """
    Todo list app index view
    """
    def get(self, request):
        return render(request, 'todo/todo.html')
