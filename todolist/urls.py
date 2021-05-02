from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodoItem, name='add'),
    path('completed/<todo_id>', views.completedTodo, name='completed'),
    path('uncompleted/<todo_id>', views.undocompletedTodo, name='uncompleted'),
    path('deletecompleted', views.deleteCompleted, name='deletecompleted'),
    path('deleteall', views.deleteAll, name='deleteall')
]
