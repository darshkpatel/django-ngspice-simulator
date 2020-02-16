"""ngspice_cloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from user_auth_app import views as auth_views
from upload_app import views as upload_views
from simulator_app import views as simulator_views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'uploads', upload_views.UploadViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('upload', upload_views.FileUploader.as_view(), name='filesUpload'),

    path('api/task/<uuid:task_id>', simulator_views.TaskResultView.as_view(), name='task_status'),
    path('api/task', simulator_views.ViewTasks.as_view(), name='view_tasks'),
    path('api/task/<uuid:task_id>/start', simulator_views.TaskStartView.as_view(), name='task_start'),
    path('api/celery/<uuid:task_id>', simulator_views.CeleryResultView.as_view(), name='celery_status'),
    
    path('api/', include(router.urls)),
    
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
    
]
