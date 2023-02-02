from django.urls import path
from .views import TodoListApiView

urlpatterns = [
    path('', TodoListApiView.as_view()),
]