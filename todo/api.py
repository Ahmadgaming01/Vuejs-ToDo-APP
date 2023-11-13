from rest_framework import viewsets
from .serializers import ToDoserializer
from .models import ToDo

class ToDoViewset(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoserializer