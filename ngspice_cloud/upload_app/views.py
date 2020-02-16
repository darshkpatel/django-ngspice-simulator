from django.shortcuts import render
from django import forms
from django.http import HttpResponse


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .serializers import FileSerializer, TaskSerializer
# from .serializers import FileSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from .models import Task




class UploadViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    # authentication_classes = (AllowAny,)
    # methods = ['POST']
    serializer_class = TaskSerializer
    parser_classes = (MultiPartParser, FormParser,)
    queryset=Task.objects.all()



class FileUploader(APIView):
    '''
    Rest API for FileUploader
    '''

    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        print(request.FILES.getlist("file"))
        serializer = TaskSerializer(data=request.data, context={'view':self})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)