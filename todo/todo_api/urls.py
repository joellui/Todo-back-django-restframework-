from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-Overview'),
    path('task-list/', views.taskList),
    path('task-detail/<int:todo_id>', views.taskDetail),
    path('task-update/<int:todo_id>', views.taskUpdate),
    path('task-create', views.taskCreate),
    path('task-delete/<int:todo_id>', views.taskDelete)
]