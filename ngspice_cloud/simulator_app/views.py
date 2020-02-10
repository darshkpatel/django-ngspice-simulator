from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny 
from celery.result import AsyncResult

class TaskResultView(APIView):
    permission_classes = (AllowAny,)             
    methods = ['GET']
    def get(self, request, task_id):
        result = AsyncResult(task_id)
        response_data = {
        'state': result.state,
        'details': result.info,
        }
        return Response(response_data)