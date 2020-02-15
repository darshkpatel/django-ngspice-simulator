from django.shortcuts import render
import json
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from celery.result import AsyncResult
from upload_app.models import Task
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from upload_app.serializers import TaskSerializer
from rest_framework.exceptions import ValidationError
from simulator_app.tasks import process_task
class TaskResultView(APIView):
    permission_classes = (AllowAny,)
    methods = ['GET']

    def get(self, request, task_id):

        if isinstance(task_id, uuid.UUID):
            celery_result = AsyncResult(str(task_id))
            task = get_object_or_404(Task, task_id=task_id)
            serializer = TaskSerializer(task, many=False)
            response_data = {
                'state': celery_result.state,
                'details': serializer.data
            }
            return Response(response_data)
        else:
            raise ValidationError('Invalid uuid format')
class CeleryResultView(APIView):
    permission_classes = (AllowAny,)
    methods = ['GET']

    def get(self, request, task_id):

        if isinstance(task_id, uuid.UUID):
            celery_result = AsyncResult(str(task_id))
            response_data = {
                'state': celery_result.state,
                'details': celery_result.info
            }
            return Response(response_data)
        else:
            raise ValidationError('Invalid uuid format')

class TaskStartView(APIView):
    permission_classes = (AllowAny,)
    methods = ['GET']

    def get(self, request, task_id):

        if isinstance(task_id, uuid.UUID):
            group_task = process_task.apply_async(kwargs={'task_id':str(task_id)}, task_id=str(task_id))
            celery_result = AsyncResult(str(task_id))
            task = get_object_or_404(Task, task_id=task_id)
            serializer = TaskSerializer(task, many=False)
            response_data = {
                'state': group_task.state,
                'details': serializer.data,
            }
            return Response(response_data)
        else:
            raise ValidationError('Invalid uuid format')

class ViewTasks(APIView):
    permission_classes = (AllowAny,)
    methods = ['GET']

    def get(self, request):
        task_list = Task.objects.all()
        serializer = TaskSerializer(task_list, many=True)
        return Response({"tasks":serializer.data})
