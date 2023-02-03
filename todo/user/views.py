from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login

from .serializers import UserSerializer, RegisterSerializer, LoginSerializer

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class UserDetailAPIView(generics.RetrieveAPIView):
    permission_classes=(permissions.IsAuthenticated, )
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class LoginAPIView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({'token': user['token']})

class LogoutAPIView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response({"detail": "Logout Successful"}, status=status.HTTP_200_OK)


        