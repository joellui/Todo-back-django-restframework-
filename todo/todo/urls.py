from django.contrib import admin
from django.urls import path, include
from todo_api import urls as todo_urls
from user import urls as user_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(user_urls)),
    path('todos/', include(todo_urls))
]
