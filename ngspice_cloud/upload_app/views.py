from django.shortcuts import render
from django import forms
from django.http import HttpResponse


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .serializers import FileSerializer, TaskSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from .models import Task


class UploadViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    # authentication_classes = (AllowAny,)
    methods = ['POST']
    serializer_class = TaskSerializer
    parser_classes = (MultiPartParser, FormParser,)
    queryset = Task.objects.all()
