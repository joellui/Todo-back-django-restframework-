from django.urls import path
from .views import UserCreateAPIView, LoginAPIView, LogoutAPIView, UserDetailAPIView

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('user/', UserDetailAPIView.as_view(), name='user-detail'),
]