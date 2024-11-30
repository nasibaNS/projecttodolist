from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import TaskSerializer
from .models import Task
from rest_framework.filters import SearchFilter


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['completed']
    search_fields = ['title']
    permission_classes = [permissions.IsAuthenticated]

