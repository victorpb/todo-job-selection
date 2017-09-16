from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^todo-list/$', views.TodoView.as_view(), name='todo-list')
]
