from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from todo_api.serializers import TodoSerializer
from  .models import Todo

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/task-list/',
        'Detail View' : '/task-detail/<int:id>/',
        'Create' : '/task-create/',
        'Update' : '/task-update/<int:id>/',
        'Delete' : '/task-delete/<int:id>/',
    }
    return Response(api_urls, status=status.HTTP_200_OK)

@api_view(['GET'])
def taskList(request):
    todos = Todo.objects.filter(user = request.user.id)
    serializer = TodoSerializer(todos,many= True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Get Task List
@api_view(['GET'])
def taskDetail(request, todo_id):
    tasks = Todo.objects.get(id=todo_id)
    serialize = TodoSerializer(tasks, many=False)
    return Response(serialize.data, status=status.HTTP_200_OK)

# Update Task
@api_view(['POST'])
def taskUpdate(request, todo_id):
    task = Todo.objects.get(id=todo_id)
    serializer = TodoSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)

# Create Task
@api_view(['POST'])
def taskCreate(request):

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

# Delete Task
@api_view(['DELETE'])
def taskDelete(request, todo_id):
    task = Todo.objects.get(id = todo_id)
    task.delete()
    return Response(status=status.HTTP_508_LOOP_DETECTED)
    