from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import TaskSerializer
from rest_framework import viewsets
from .models import Task


class UploadViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    authentication_classes = (AllowAny,)
    methods = ['POST']
    serializer_class = TaskSerializer
    parser_classes = (MultiPartParser, FormParser,)
    queryset = Task.objects.all()
