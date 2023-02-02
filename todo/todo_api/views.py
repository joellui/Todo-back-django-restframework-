from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from todo_api.serializers import TodoSerializer
from  .models import Todo

class TodoListApiView(APIView):
    # Check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # List all
    def get(self, request):
        # all todo for given user
        todos = Todo.objects.filter(user = request.user.id)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Create
    def post(self, request):
        # create the todo
        data = {
            'task': request.data.get('task'),
            'completed': request.data.get('completed'),
            'user': request.user.id
        }
        serializer = TodoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
